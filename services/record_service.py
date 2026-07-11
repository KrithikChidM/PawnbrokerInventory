
import csv
import os
import shutil
from datetime import date

from database import Database
from config import DATABASE_NAME, BACKUP_PATH


class RecordService:
    def __init__(self):
        self.db = Database()

    def check_balance(self):
        row = self.db.fetchone(
            """
            SELECT Total
            FROM Entries
            ORDER BY rowid DESC
            LIMIT 1
            """
        )

        if row is None:
            return 0.00

        return float(row[0])

    def start_new_record(self, last_balance):
        today = date.today()

        folder_name = f"{today.year-1}_{today.year}"
        backup_folder = os.path.join(BACKUP_PATH, folder_name)

        os.makedirs(backup_folder, exist_ok=True)

        # Backup database
        shutil.copy2(
            DATABASE_NAME,
            os.path.join(
                backup_folder,
                "ChitFundApplication.db"
            )
        )

        # Backup Entries table
        rows = self.db.fetchall(
            """
            SELECT *
            FROM Entries
            """
        )

        with open(
            os.path.join(backup_folder, "backup.csv"),
            "w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.writer(file)

            writer.writerow([
                "Date",
                "CustName",
                "ChitNo",
                "Info",
                "Weight",
                "Status",
                "Months",
                "Principal",
                "InAmt",
                "InterAmt",
                "OutAmt",
                "Total"
            ])

            writer.writerows(rows)

        # Delete closed records
        self.db.execute(
            """
            DELETE FROM Entries
            WHERE Status != 0
            """
        )

        # Insert New FY Balance record
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
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                str(today),
                None,
                None,
                "New FY Balance",
                None,
                2,
                None,
                None,
                None,
                None,
                None,
                float(last_balance)
            )
        )