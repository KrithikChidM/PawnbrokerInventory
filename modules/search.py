import tkinter as tk
from tkinter import ttk, messagebox

from database import Database


class Search(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.db = Database()

        self.title("Search")
        self.geometry("1100x500")
        self.resizable(False, False)

        tk.Label(
            self,
            text="Search Customer Records",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        top_frame = tk.Frame(self)
        top_frame.pack(pady=10)

        tk.Label(
            top_frame,
            text="Name"
        ).grid(row=0, column=0, padx=5)

        self.customer = ttk.Combobox(
            top_frame,
            width=40,
            state="readonly"
        )
        self.customer.grid(row=0, column=1, padx=5)

        tk.Button(
            top_frame,
            text="Submit",
            width=12,
            command=self.search
        ).grid(row=0, column=2, padx=5)

        columns = (
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
        )

        self.table = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=16
        )

        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=85, anchor="center")

        self.table.pack(fill="both", padx=10, pady=10)

        self.load_customers()

    def load_customers(self):
        rows = self.db.fetchall(
            "SELECT CID, CName FROM Customer ORDER BY CName"
        )

        values = [
            f"{cid} | {name}"
            for cid, name in rows
        ]

        self.customer["values"] = values

        if values:
            self.customer.current(0)

    def search(self):
        if not self.customer.get():
            messagebox.showerror(
                "Error",
                "Select a customer."
            )
            return

        cname = self.customer.get().split(" | ", 1)[1]

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
                   OutAmt,
                   Total
            FROM Entries
            WHERE CustName=?
            """,
            (cname,)
        )

        for item in self.table.get_children():
            self.table.delete(item)

        for row in rows:
            self.table.insert("", tk.END, values=row)
