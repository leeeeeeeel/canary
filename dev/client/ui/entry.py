""" """

import tkinter as tk

class Entry(tk.Frame):

    f_signup = None
    f_signin = None

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller

        self.initUI()

    def initUI(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        f_sign = tk.Frame(self)
        f_sign.columnconfigure(0, weight=1)
        f_sign.rowconfigure(0, weight=1)
        f_sign.grid(sticky=tk.E+tk.W+tk.S+tk.N, row=1, column=1)

        self.f_signup = SignUp(parent=f_sign, controller=self)
        self.f_signin = SignIn(parent=f_sign, controller=self)

        self.show_frame(SignUp)

    def show_frame(self, frame):
        if frame.__name__ == SignUp.__name__ and self.f_signup != None:
            self.f_signup.tkraise()
        if frame.__name__ == SignIn.__name__ and self.f_signin != None:
            self.f_signin.tkraise()

class SignUp(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller

        self.initUI()

    def initUI(self):
        self.grid(row=0, column=0, sticky="nsew")

        self.b_signup = tk.Button(self, text="sign-up", command=self.b_signup_click)
        self.b_signup.pack(fill=tk.BOTH, expand=True)

    def b_signup_click(self):
        self.controller.show_frame(SignIn)

class SignIn(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller

        self.initUI()

    def initUI(self):
        self.grid(row=0, column=0, sticky="nsew")

        self.b_signin = tk.Button(self, text="sign-in", command=self.b_signin_click)
        self.b_signin.pack(fill=tk.BOTH, expand=True)

    def b_signin_click(self):
        self.controller.show_frame(SignUp)
