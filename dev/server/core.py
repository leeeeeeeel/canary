""" Canary server """

from net import server
from ui import input_handler

def main():
    s = server.Server()
    s.listen_async()
    input_handler.listen(s)

if __name__ == "__main__":
    main()
