""" """

import threading as t

import net.server as s

class ConnectionHandler(t.Thread):

    def __init__(self, controller, connection, client_address):
        super(ConnectionHandler, self).__init__()
        self.controller = controller
        self.connection = connection
        self.client_address = client_address

    def run(self):
        print("connection from %s:%d" % self.client_address)

        data = self.connection.recv(self.controller.BUFFER_SIZE).decode()

        if data:
            self.handle(data)

        self.connection.close()
        print("finished %s:%d connection" % self.client_address)

    def handle(self, data):
        print(data)
