""" """

import tkinter as tk

import help as h
import ui.app.entry_signin as si
import ui.app.entry_signup as su

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

        self.f_signin = si.SignIn(parent=f_sign, controller=self)
        self.f_signup = su.SignUp(parent=f_sign, controller=self)

        self.f_signin.grid(row=0, column=0, sticky="nsew")
        self.f_signup.grid(row=0, column=0, sticky="nsew")

        self.show_frame("sign-up")

    def signin(self, email, username, password, confirm_password):
        valid = True

        if not h.EMAIL_REGEX.match(email):
            # TODO
            valid = False
        if not h.USERNAME_REGEX.match(username):
            # TODO
            valid = False
        if not h.PASSWORD_REGEX.match(password):
            # TODO
            valid = False
        if not password == confirm_password:
            # TODO
            valid = False

        if valid:
            self.controller.signin(email, username, password)

    def signup(self, email, password):
        valid = True

        if not h.EMAIL_REGEX.match(email):
            # TODO
            valid = False
        if not h.PASSWORD_REGEX.match(password):
            # TODO
            valid = False

        if valid:
            self.controller.signup(email, password)

    def show_frame(self, frame_name):
        if frame_name =="sign-in":
            self.f_signin.tkraise()
        if frame_name == "sign-up":
            self.f_signup.tkraise()
