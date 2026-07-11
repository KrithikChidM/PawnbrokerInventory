from datetime import date

import config
from database import Database


class ChitService:
    def __init__(self):
        self.db = Database()

    def open_chit(self, name, info, weight, amount):
        # Check whether current chit number already exists as an open chit
        existing = self.db.fetchone(
            """
            SELECT ChitNo
            FROM Entries
            WHERE Status=0 AND ChitNo=?
            """,
            (str(config.chit_no),)
        )

        if existing:
            raise Exception("Chit number already exists.")

        # Check chit number range
        if config.Start_chit and config.End_Chit:
            if not (
                int(config.Start_chit)
                <= config.chit_no
                <= int(config.End_Chit)
            ):
                raise Exception("Chit number is outside the configured range.")

        # Running total
        last_total = self.db.fetchone(
            """
            SELECT Total
            FROM Entries
            ORDER BY rowid DESC
            LIMIT 1
            """
        )

        previous_total = 0.00 if last_total is None else float(last_total[0])

        current_total = -float(amount)
        total = round(previous_total + current_total, 2)

        self.db.execute(
            """
            INSERT INTO Entries
            (
                Date,
                CustName,
                ChitNo,
                Info,
                Weight,
                Status,
                Months,
                Principal,
                InAmt,
                InterAmt,
                OutAmt,
                Total
            )
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                str(date.today()),
                name,
                str(config.chit_no),
                info,
                str(weight),
                0,
                0,
                0.00,
                0.00,
                0.00,
                float(amount),
                total
            )
        )

        self.db.execute(
            """
            INSERT INTO Available
            (ChitNo, Info, Weight)
            VALUES (?,?,?)
            """,
            (
                str(config.chit_no),
                info,
                str(weight)
            )
        )

        config.chit_no += 1

    def get_close_details(self, chit_no):
        row = self.db.fetchone(
            """
            SELECT Date,
                   CustName,
                   ChitNo,
                   Info,
                   Weight,
                   abs(OutAmt)
            FROM Entries
            WHERE ChitNo=? AND Status=0
            """,
            (chit_no,)
        )

        if row is None:
            return None

        open_date = date.fromisoformat(row[0])
        today = date.today()

        months = abs(
            (today.year - open_date.year) * 12
            + (today.month - open_date.month)
        )

        principal = float(row[5])

        interest = principal * (
            1 + (config.interest_value * months * 0.01)
        )

        return (
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            months,
            round(principal, 2),
            round(interest, 2)
        )

    def close_chit(self, chit_no):
        details = self.get_close_details(chit_no)

        if details is None:
            return

        # Running total
        last_total = self.db.fetchone(
            """
            SELECT Total
            FROM Entries
            ORDER BY rowid DESC
            LIMIT 1
            """
        )

        previous_total = 0.00 if last_total is None else float(last_total[0])
        total = round(previous_total + details[7], 2)

        self.db.execute(
            """
            INSERT INTO Entries
            (
                Date,
                CustName,
                ChitNo,
                Info,
                Weight,
                Status,
                Months,
                Principal,
                InAmt,
                InterAmt,
                OutAmt,
                Total
            )
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                str(date.today()),
                details[1],
                details[2],
                details[3],
                details[4],
                1,
                details[5],
                details[6],
                0.00,
                details[7],
                0.00,
                total
            )
        )

        self.db.execute(
            """
            UPDATE Entries
            SET Status=1
            WHERE ChitNo=? AND Status=0
            """,
            (chit_no,)
        )

        self.db.execute(
            "DELETE FROM Available WHERE ChitNo=?",
            (chit_no,)
        )
