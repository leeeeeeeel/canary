""" """

import socket as s
import threading as t

import net.handler as h

class Server:

    BUFFER_SIZE = 1024
    PORT = 4242

    clients = []
    threads = []

    def __init__(self):
        self.address = ("localhost", self.PORT)

        self.sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        self.sock.bind(self.address)
        self.sock.listen(True)

        print ("started up on %s port %s." % self.address)
        self.running = True

    def shut(self):
        self.running = False

        s.socket(s.AF_INET,
                  s.SOCK_STREAM).connect(self.address)

        self.sock.close()

        for t in self.threads:
            t.join()

        print ("shuted down.")

    def listen_async(self):
        newthread = t.Thread(target=self.listen)
        newthread.start()
        self.threads.append(newthread)

    def listen(self):
        print ("listening for connections...")
        while self.running:
            try:
                conn, addr = self.sock.accept()

                newhandler = h.ConnectionHandler(
                    controller=self,
                    connection=conn,
                    client_address=addr)
                newhandler.start()
                self.threads.append(newhandler)
            except (OSError):
                pass
        print("terminated listening.")
