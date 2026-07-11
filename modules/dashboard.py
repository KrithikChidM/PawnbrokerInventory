import tkinter as tk

from modules.open_chit import OpenChit
from modules.close_chit import CloseChit
from modules.reports import Reports
from modules.search import Search
from modules.customer import Customer
from modules.settings import Settings
from modules.start_new_record import StartNewRecord


class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Chit Fund Application")
        self.geometry("600x450")
        self.resizable(True, True)

        tk.Label(
            self,
            text="Chit Fund Application",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        buttons = [
            ("Open a Chit", self.open_chit),
            ("Close a Chit", self.close_chit),
            ("Generate Report", self.generate_report),
            ("Start New Record", self.start_new_record),
            ("General Settings", self.general_settings),
            ("Add Customer", self.add_customer),
            ("Search", self.search),
        ]

        for text, command in buttons:
            tk.Button(
                button_frame,
                text=text,
                width=25,
                height=2,
                command=command
            ).pack(pady=5)

    def open_chit(self):
        OpenChit(self)

    def close_chit(self):
        CloseChit(self)

    def generate_report(self):
        Reports(self)

    def start_new_record(self):
        StartNewRecord(self)

    def general_settings(self):
        Settings(self)

    def add_customer(self):
        Customer(self)

    def search(self):
        Search(self)