""" """

import tkinter as tk

import ui.app.entry as e
import ui.app.main as m

class Root(tk.Tk):

    def __init__(self, client):
        tk.Tk.__init__(self)
        self.client = client

        self.initUI()
 
    def initUI(self):
        self.geometry("%dx%d+0+0" % (900, 600))

        self.f_current = e.Entry(parent=self, controller=self)
        self.f_current.pack(fill="both", expand=True)

    def sign_in(email, username, password):
        # TODO
        pass

    def sign_up(email, password):
        # TODO
        pass

    def start_session(self, token):
        # TODO
        pass

    def finish_session(self):
        # TODO
        pass
