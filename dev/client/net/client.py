""" """

import pickle
import socket
import threading

from net.msg import msg
from net.msg.authentication import *

class Client:

    BUFFER_SIZE = 1024
    SERVER_ADDRESS = ("localhost", 4242)

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)
        self.sock.connect(Client.SERVER_ADDRESS)
        self.al_thread = False

        self.connected = True

    def reconnect(self):
        pass

    def disconnect(self, join=False):
        if not self.connected:
            return

        self.connected = False

        self.sock.close()

        if join:
            self.al_thread.join()

        print("disconnected from server.")

    def send(self, message):
        data = pickle.dumps(message, pickle.HIGHEST_PROTOCOL)
        self.sock.sendall(data)
        print("sent %d bytes to server" % len(data))

    def listen_async(self):
        self.al_thread = threading.Thread(
            target=self.listen,
            name="listen_thread")
        self.al_thread.start()

    def listen(self):
        try:
            while self.connected:
                data = self.sock.recv(self.BUFFER_SIZE)

                if data:
                    message = pickle.loads(data)
                    self.handle(message)
        except (ConnectionAbortedError, ConnectionResetError) as e:
            # disconnection from either sides
            pass
        except Exception as e:
            print("exception: '%s', terminating connection" % e)

        self.disconnect()

    def handle(self, message):
        print("message received")

        if not isinstance(message, msg.MsgRoot):
            raise RuntimeError("invalid message")

        if message.messageType == msg.NONE:
            self.none_msg(message)
        elif message.messageType == msg.ON_SIGN_IN:
            self.on_signin_msg(message)
        elif message.messageType == msg.ON_SIGN_UP:
            self.on_signon_msg(message)

        print("finished handle of message")

    def none_msg(self, message):
        print("none")

    def on_signin_msg(self, message):
        print("on_sign_in")

    def on_signon_msg(self, message):
        print("on_sign_on")
