""" """

import socket
import threading

import help
from net import client

class Server:

    BUFFER_SIZE = 1024
    ADDRESS = ("127.0.0.1", 4242)

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)
        self.sock.bind(self.ADDRESS)
        self.sock.listen(True)

        self.al_thread = False

        self.clients = []

        print("started up on %s port %s." % self.ADDRESS)
        self.running = True

    def shut(self):
        self.running = False

        # free self.sock from accept()
        socket.socket(socket.AF_INET,
                 socket.SOCK_STREAM).connect(self.ADDRESS)

        if self.al_thread:
            self.al_thread.join()

        self.sock.close()

        for c in self.clients:
            c.disconnect(join=True)

        print("shutted down.")

    def listen_async(self):
        self.al_thread = threading.Thread(
            target=self.listen,
            name="listen_thread")
        self.al_thread.start()

    def listen(self):
        print("listening for connections...")

        while self.running:
            conn, addr = self.sock.accept()
            name = help.anon_username()

            print("received connection from %s:%d as %s"
                % (addr[0], addr[1], name))

            newclient = client.Client(
                server = self,
                connection=conn,
                address=addr,
                username=name)

            self.clients.append(newclient)

        print("terminated listening for connections.")
