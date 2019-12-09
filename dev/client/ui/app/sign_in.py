""" """

import tkinter as tk

import ui.consts as c

class SignIn(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller

        self.initUI()

    def initUI(self):
        self.configure()

        f_components = tk.Frame(self)
        f_components.rowconfigure(0, pad=10)
        f_components.rowconfigure(1, pad=10)
        f_components.rowconfigure(2, pad=10)
        f_components.rowconfigure(3, pad=10)
        f_components.rowconfigure(4, pad=10)
        f_components.rowconfigure(5, pad=10)
        f_components.rowconfigure(6, pad=10)
        f_components.rowconfigure(7, pad=10)
        f_components.rowconfigure(8, pad=10)
        f_components.rowconfigure(9, pad=10)
        f_components.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        l_email = tk.Label(
            f_components,
            text="email:",
            anchor="e",
            font=c.label_font_beta)

        self.e_email = tk.Entry(
            f_components,
            font=c.entry_font_alpha)

        l_username = tk.Label(
            f_components,
            text="username:",
            anchor="e",
            font=c.label_font_beta)

        self.e_username = tk.Entry(
            f_components,
            font=c.entry_font_alpha)

        l_password = tk.Label(
            f_components,
            text="password:",
            anchor="e",
            font=c.label_font_beta)

        self.e_password = tk.Entry(
            f_components,
            font=c.entry_font_alpha)

        l_confirm_password = tk.Label(
            f_components,
            text="confirm password:",
            anchor="e",
            font=c.label_font_beta)

        self.e_confirm_password = tk.Entry(
            f_components,
            font=c.entry_font_alpha)

        b_signin = tk.Button(
            f_components,
            text="sign-in",
            command=self.b_signin_click,
            font=c.button_font_alpha)

        l_have_account = tk.Label(
            f_components,
            text="Already have an account? Sign-up!",
            anchor="c",
            font=c.label_font_gama)
        l_have_account.bind(
            "<Button-1>", self.l_have_account_click)

        l_email.grid(row=0, column=0)
        self.e_email.grid(row=1, column=0)
        l_username.grid(row=2, column=0)
        self.e_username.grid(row=3, column=0)
        l_password.grid(row=4, column=0)
        self.e_password.grid(row=5, column=0)
        l_confirm_password.grid(row=6, column=0)
        self.e_confirm_password.grid(row=7, column=0)
        b_signin.grid(row=8, column=0)
        l_have_account.grid(row=9, column=0)

    def b_signin_click(self):
        email = self.e_email.get()
        username = self.e_username.get()
        password = self.e_password.get()
        confirm_password = self.e_confirm_password.get()

        self.controller.sign_in(email, username, password, confirm_password)

    def l_have_account_click(self, event=None):
        self.controller.show_frame("sign-up")
