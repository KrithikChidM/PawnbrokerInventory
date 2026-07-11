import csv
import os

from database import Database
from config import REPORT_PATH


class ReportService:
    def __init__(self):
        self.db = Database()

    def generate_report(self, start_date, end_date):
        rows = self.db.fetchall(
            """
            SELECT Date,
                   CustName,
                   ChitNo,
                   Info,
                   Weight,
                   Status,
                   Months,
                   Principal,
                   InAmt,
                   InterAmt,
                   abs(OutAmt),
                   abs(Total)
            FROM Entries
            WHERE Date BETWEEN ? AND ?
            ORDER BY Date
            """,
            (start_date, end_date)
        )

        os.makedirs(REPORT_PATH, exist_ok=True)

        filename = f"{start_date}_to_{end_date}.csv"
        filepath = os.path.join(REPORT_PATH, filename)

        with open(filepath, "w", newline="", encoding="utf-8") as file:
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

        return filepath

