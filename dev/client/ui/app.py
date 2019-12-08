""" """

import tkinter as tk

class App(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.p_statusbar = Statusbar(self)
        self.p_toolbar = Toolbar(self)
        self.p_navbar = Navbar(self)
        self.p_main = Main(self)

        self.p_statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.p_toolbar.pack(side=tk.TOP, fill=tk.X)
        self.p_navbar.pack(side=tk.LEFT, fill=tk.Y)
        self.p_main.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

class Navbar(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        pass

class Toolbar(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        pass

class Statusbar(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        pass

class Main(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        pass
