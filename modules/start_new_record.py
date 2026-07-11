import tkinter as tk
from tkinter import messagebox

from services.record_service import RecordService


class StartNewRecord(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.service = RecordService()

        self.title("Start New Record")
        self.geometry("420x180")
        self.resizable(False, False)

        tk.Label(
            self,
            text="Last Balance"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.last_balance = tk.Entry(self, width=25)
        self.last_balance.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(
            self,
            text="Check Balance",
            width=15,
            command=self.check_balance
        ).grid(row=1, column=0, padx=10, pady=10)

        tk.Button(
            self,
            text="Submit",
            width=15,
            command=self.submit
        ).grid(row=1, column=1, padx=10, pady=10)

    def check_balance(self):
        try:
            balance = self.service.check_balance()

            self.last_balance.delete(0, tk.END)
            self.last_balance.insert(0, str(balance))

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def submit(self):
        try:
            self.service.start_new_record(
                float(self.last_balance.get())
            )

            messagebox.showinfo(
                "Success",
                "New financial record started successfully."
            )

            self.destroy()

        except Exception as e:
            messagebox.showerror("Error", str(e))

