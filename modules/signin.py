import tkinter as tk
from tkinter import messagebox
from modules.dashboard import Dashboard


class SignIn(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Chit Fund Application - Sign In")
        self.geometry("400x220")
        self.resizable(False, False)

        tk.Label(
            self,
            text="Sign In",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        tk.Label(self, text="Username").pack()
        self.username = tk.Entry(self, width=30)
        self.username.pack(pady=5)

        tk.Label(self, text="Password").pack()
        self.password = tk.Entry(self, width=30, show="*")
        self.password.pack(pady=5)

        # Press Enter to Sign In
        self.password.bind("<Return>", self.sign_in)
        self.username.bind("<Return>", self.sign_in)

    def sign_in(self, event=None):
        if self.username.get() == "admin" and self.password.get() == "admin":
            self.destroy()
            dashboard = Dashboard()
            dashboard.mainloop()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")
