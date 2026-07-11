import tkinter as tk
from tkinter import ttk, messagebox

from database import Database
from modules.customer import Customer
from services.chit_service import ChitService


class OpenChit(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.db = Database()
        self.service = ChitService()

        self.title("Open a Chit")
        self.geometry("550x420")
        self.resizable(False, False)

        tk.Label(self, text="Open a Chit", font=("Arial", 16, "bold")).pack(pady=10)

        form = tk.Frame(self)
        form.pack(fill="both", expand=True, padx=20, pady=10)

        # Customer
        tk.Label(form, text="Name").grid(row=0, column=0, sticky="w", pady=8)

        self.customer = ttk.Combobox(form, width=35, state="readonly")
        self.customer.grid(row=0, column=1, padx=5)

        tk.Button(
            form,
            text="+",
            width=3,
            command=self.add_customer
        ).grid(row=0, column=2)

        # Info
        tk.Label(form, text="Info").grid(row=1, column=0, sticky="nw", pady=8)

        self.info = tk.Text(form, width=35, height=6)
        self.info.grid(row=1, column=1, columnspan=2)

        # Weight
        tk.Label(form, text="Weight").grid(row=2, column=0, sticky="w", pady=8)

        self.weight = tk.Entry(form, width=38)
        self.weight.grid(row=2, column=1, columnspan=2)

        # Amount
        tk.Label(form, text="Amount").grid(row=3, column=0, sticky="w", pady=8)

        self.amount = tk.Entry(form, width=38)
        self.amount.grid(row=3, column=1, columnspan=2)

        # Submit
        tk.Button(
            self,
            text="Submit",
            width=15,
            command=self.submit
        ).pack(pady=15)

        self.load_customers()

    def load_customers(self):
        customers = self.db.fetchall(
            "SELECT CName FROM Customer ORDER BY CName"
        )

        self.customer["values"] = [row[0] for row in customers]

        if customers:
            self.customer.current(0)

    def add_customer(self):
        Customer(self)
        self.wait_window(self.winfo_children()[-1])
        self.load_customers()

    def submit(self):
        name = self.customer.get()
        info = self.info.get("1.0", tk.END).strip()
        weight = self.weight.get().strip()
        amount = self.amount.get().strip()

        if not name or not info or not weight or not amount:
            messagebox.showerror("Error", "All fields are mandatory.")
            return

        try:
            float(weight)
            float(amount)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Weight and Amount should be numeric."
            )
            return

        self.service.open_chit(
            name=name,
            info=info,
            weight=weight,
            amount=float(amount)
        )

        messagebox.showinfo("Success", "Value added successfully")

        self.destroy()
