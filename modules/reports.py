import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

from services.report_service import ReportService


class Reports(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.service = ReportService()

        self.title("Generate Report")
        self.geometry("420x220")
        self.resizable(False, False)

        tk.Label(
            self,
            text="Generate Report",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(
            form,
            text="Start Date"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.start_date = DateEntry(
            form,
            width=20,
            date_pattern="yyyy-mm-dd"
        )
        self.start_date.grid(row=0, column=1, padx=10)

        tk.Label(
            form,
            text="End Date"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.end_date = DateEntry(
            form,
            width=20,
            date_pattern="yyyy-mm-dd"
        )
        self.end_date.grid(row=1, column=1, padx=10)

        tk.Button(
            self,
            text="Submit",
            width=15,
            command=self.generate_report
        ).pack(pady=20)

    def generate_report(self):
        start = self.start_date.get()
        end = self.end_date.get()

        self.service.generate_report(start, end)

        messagebox.showinfo(
            "Success",
            "Report generated successfully."
        )

        self.destroy()
