""" """

from net import client
from ui import root

def main():
    c = client.Client()
    c.listen_async()
    r = root.Root(c)
    r.mainloop()

if __name__ == "__main__":
    main()
