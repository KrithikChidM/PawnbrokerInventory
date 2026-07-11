import tkinter as tk
from tkinter import messagebox

import config
from services.settings_service import SettingsService


class Settings(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.service = SettingsService()

        self.title("General Settings")
        self.geometry("420x260")
        self.resizable(False, False)

        tk.Label(
            self,
            text="General Settings",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(
            form,
            text="Interest %"
        ).grid(row=0, column=0, padx=10, pady=8, sticky="w")

        self.interest = tk.Entry(form, width=30)
        self.interest.insert(0, str(config.interest_value))
        self.interest.grid(row=0, column=1)

        tk.Label(
            form,
            text="Chit Start"
        ).grid(row=1, column=0, padx=10, pady=8, sticky="w")

        self.start_chit = tk.Entry(form, width=30)
        self.start_chit.insert(0, config.Start_chit)
        self.start_chit.grid(row=1, column=1)

        tk.Label(
            form,
            text="Chit End"
        ).grid(row=2, column=0, padx=10, pady=8, sticky="w")

        self.end_chit = tk.Entry(form, width=30)
        self.end_chit.insert(0, config.End_Chit)
        self.end_chit.grid(row=2, column=1)

        tk.Button(
            self,
            text="Submit",
            width=15,
            command=self.submit
        ).pack(pady=20)

    def submit(self):
        interest = self.interest.get().strip()
        start = self.start_chit.get().strip()
        end = self.end_chit.get().strip()

        if not interest or not start or not end:
            messagebox.showerror(
                "Error",
                "All fields are mandatory."
            )
            return

        try:
            float(interest)
            float(start)
            float(end)
        except ValueError:
            messagebox.showerror(
                "Error",
                "All values should be numeric."
            )
            return

        self.service.update_settings(
            float(interest),
            start,
            end
        )

        messagebox.showinfo(
            "Success",
            "Settings updated successfully."
        )

        self.destroy()
