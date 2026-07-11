import tkinter as tk
from tkinter import ttk, messagebox

from database import Database
from services.chit_service import ChitService


class CloseChit(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.db = Database()
        self.service = ChitService()

        self.title("Close a Chit")
        self.geometry("700x450")
        self.resizable(False, False)

        tk.Label(
            self,
            text="Close a Chit",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        top_frame = tk.Frame(self)
        top_frame.pack(pady=10)

        tk.Label(
            top_frame,
            text="Chit Number"
        ).grid(row=0, column=0, padx=5)

        self.chit_no = ttk.Combobox(
            top_frame,
            width=30,
            state="readonly"
        )
        self.chit_no.grid(row=0, column=1, padx=5)

        tk.Button(
            top_frame,
            text="Submit",
            width=12,
            command=self.submit
        ).grid(row=0, column=2, padx=5)

        self.close_btn = tk.Button(
            top_frame,
            text="Close",
            width=12,
            state=tk.DISABLED,
            command=self.close_chit
        )
        self.close_btn.grid(row=0, column=3, padx=5)

        columns = (
            "Date",
            "Customer",
            "Chit No",
            "Info",
            "Weight",
            "Months",
            "Principal",
            "Interest"
        )

        self.table = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=12
        )

        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, anchor="center", width=85)

        self.table.pack(fill="both", padx=10, pady=10)

        self.record = None

        self.load_chits()

    def load_chits(self):
        rows = self.db.fetchall(
            "SELECT ChitNo FROM Entries WHERE Status=0 ORDER BY ChitNo"
        )

        self.chit_no["values"] = [row[0] for row in rows]

        if rows:
            self.chit_no.current(0)

    def submit(self):
        chit = self.chit_no.get()

        if not chit:
            messagebox.showerror("Error", "Select a chit number.")
            return

        self.record = self.service.get_close_details(chit)

        if not self.record:
            messagebox.showerror("Error", "Record not found.")
            return

        for item in self.table.get_children():
            self.table.delete(item)

        self.table.insert("", tk.END, values=self.record)

        self.close_btn.config(state=tk.NORMAL)

    def close_chit(self):
        if not self.record:
            return

        choice = messagebox.askyesno(
            "Confirmation",
            "Do you want to close this chit?"
        )

        if not choice:
            return

        self.service.close_chit(self.chit_no.get())

        messagebox.showinfo(
            "Success",
            "Chit closed successfully."
        )

        self.destroy()
