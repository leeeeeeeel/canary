""" """

import tkinter as tk

import net.client as c
import ui.root as r

def main():
    client = c.Client()
    root = r.Root(client)
    root.mainloop()

if __name__ == "__main__":
    main()
