""" """

import tkinter as tk

import ui.entry as e
import ui.app as a

class Root(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.initUI()

    def initUI(self):
        self.geometry("%dx%d+0+0" % (900, 600))

        self.f_current = e.Entry(parent=self, controller=self)
        self.f_current.pack(fill="both", expand=True)

    def start_session(self, token):
        # TODO
        pass

    def finish_session(self):
        # TODO
        pass
