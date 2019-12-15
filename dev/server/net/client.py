""" """

from net import server
from net import handler

class Client:
    def __init__(self, server, connection, address, username):
        self.server = server
        self.connection = connection
        self.address = address
        self.username = username

        self.connected = True

        self.handler = handler.ClientHandler(
            server=server,
            client=self)
        self.handler.start()

    def reconnect(self):
        pass

    def disconnect(self, join=False):
        if not self.connected:
            return

        self.connected = False

        self.connection.close()

        if join:
            self.handler.join()

        print("%s disconnected" % self.username)
