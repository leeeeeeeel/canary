import socket as s

class Server:

    BUFFER_SIZE = 1024

    def __init__():
        pass

    def start(self, ip="localhost", port=8080):
        self.running = True
        self.address = (ip, port)
        self.sock = s.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(self.address)

        print ("started up on %s port %s" % self.address)

        self.listen()

    def shut(self):
        self.running = False
        self.sock.close()

        print ("shutted down.")

    def listen():
        sock.listen(True)

        print ("listening for connections..."")
        while self.running:
            connection, client_address = sock.accept()

            handler = connection_handler(self, connection, client_address)
            handler.handle_async()

            connection.close()
