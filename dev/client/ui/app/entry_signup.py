""" """

import tkinter as tk

import ui.consts as c

class SignUp(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller

        self.initUI()

    def initUI(self):
        self.configure()

        f_components = tk.Frame(self)
        f_components.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        l_email = tk.Label(
            f_components,
            text="email:",
            anchor="e",
            font=c.label_font_beta)

        self.e_email = tk.Entry(
            f_components,
            font=c.entry_font_alpha)

        l_password = tk.Label(
            f_components,
            text="password:",
            anchor="e",
            font=c.label_font_beta)

        l_forgot_password = tk.Label(
            f_components,
            text="forgot password?",
            anchor="w",
            font=c.label_font_beta)
        l_forgot_password.bind(
            "<Button-1>", self.l_forgot_password_click)

        self.e_password = tk.Entry(
            f_components,
            font=c.entry_font_alpha)

        b_signup = tk.Button(
            f_components,
            text="sign-up",
            command=self.b_signup_click,
            font=c.button_font_alpha)

        l_create_account = tk.Label(
            f_components,
            text="Don't have an account? Sign-in for free!",
            anchor="c",
            font=c.label_font_gama)
        l_create_account.bind(
            "<Button-1>", self.l_create_account_click)

        l_email.grid(row=0, column=0, sticky="w")
        self.e_email.grid(row=1, column=0, columnspan=2)
        l_password.grid(row=2, column=0, sticky="w", pady=(10, 0))
        l_forgot_password.grid(row=2, column=1, sticky="e", pady=(10, 0))
        self.e_password.grid(row=3, column=0, columnspan=2)
        b_signup.grid(row=4, column=0, columnspan=2, pady=10)
        l_create_account.grid(row=5, column=0, columnspan=2)

    def l_forgot_password_click(self, event=None):
        # TODO
        pass

    def b_signup_click(self, event=None):
        email = self.e_email.get()
        password = self.e_password.get()

        self.controller.sign_up(email, password)

    def l_create_account_click(self, event=None):
        self.controller.show_frame("sign-in")
