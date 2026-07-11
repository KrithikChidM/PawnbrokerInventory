import tkinter as tk
from tkinter import messagebox

from services.customer_service import CustomerService


class Customer(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.service = CustomerService()

        self.title("Add Customer")
        self.geometry("400x220")
        self.resizable(False, False)

        tk.Label(
            self,
            text="Add Customer",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(
            form,
            text="Customer ID"
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.cid = tk.Entry(form, width=30)
        self.cid.grid(row=0, column=1)

        tk.Label(
            form,
            text="Customer Name"
        ).grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.cname = tk.Entry(form, width=30)
        self.cname.grid(row=1, column=1)

        tk.Button(
            self,
            text="Submit",
            width=15,
            command=self.submit
        ).pack(pady=20)

    def submit(self):
        cid = self.cid.get().strip()
        cname = self.cname.get().strip()

        if not cid or not cname:
            messagebox.showerror(
                "Error",
                "All fields are mandatory."
            )
            return

        try:
            int(cid)
        except ValueError:
            messagebox.showerror(
                "Error",
                "Customer ID should be an integer."
            )
            return

        self.service.add_customer(cid, cname)

        messagebox.showinfo(
            "Success",
            "Customer added successfully."
        )

        self.destroy()
