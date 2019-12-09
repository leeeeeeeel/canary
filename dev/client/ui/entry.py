""" """

import tkinter as tk

import ui.constants as consts

large_font = ('Verdana',15)
small_font = ('Verdana',10)

class Entry(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller

        self.initUI()

    def initUI(self):
        self.configure(background='black')

        self.columnconfigure(0, weight=True)
        self.columnconfigure(2, weight=True)
        self.rowconfigure(0, weight=True)
        self.rowconfigure(2, weight=True)

        f_sign = tk.Frame(self)
        f_sign.columnconfigure(0, weight=True)
        f_sign.rowconfigure(0, weight=True)
        f_sign.grid(sticky="nsew", row=1, column=1)

        self.f_signup = SignUp(parent=f_sign, controller=self)
        self.f_signup.grid(row=0, column=0, sticky="nsew")

        self.f_signin = SignIn(parent=f_sign, controller=self)
        self.f_signin.grid(row=0, column=0, sticky="nsew")

        self.show_frame(SignUp)

    def show_frame(self, frame):
        if frame == SignUp:
            self.f_signup.tkraise()
        if frame == SignIn:
            self.f_signin.tkraise()

class SignUp(tk.Frame):

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
        f_components.grid(row=0, column=0, padx=20, pady=20)

        e_email = tk.Entry(f_components, font=consts.entry_font_alpha)
        e_email.grid(row=1, column=0, columnspan=2)

        l_password = tk.Label(f_components, text="password:", anchor="e", font=consts.entry_font_beta)
        l_password.grid(row=2, column=0)

        l_forgot_password = tk.Label(f_components, text="forgot password?", anchor="w", font=consts.entry_font_beta)
        l_forgot_password.grid(row=2, column=1)

        e_password = tk.Entry(f_components, font=consts.entry_font_alpha)
        e_password.grid(row=3, column=0, columnspan=2)

        b_signup = tk.Button(f_components, text="sign-up", command=self.b_signup_click)
        b_signup.grid(row=5, column=0, columnspan=2)

    def b_signup_click(self):
        self.controller.show_frame(SignIn)

class SignIn(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller

        self.initUI()

    def initUI(self):
        self.configure()

        b_signin = tk.Button(self, text="sign-in", command=self.b_signin_click)
        b_signin.pack(fill=tk.BOTH, expand=True)

    def b_signin_click(self):
        self.controller.show_frame(SignUp)
