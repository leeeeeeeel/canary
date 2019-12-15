""" """

import pickle
import threading

from net.msg import msg
from net.msg.authentication import *

class ClientHandler(threading.Thread):

    def __init__(self, server, client):
        super(ClientHandler, self).__init__(
            name="%s_thread" % client.username)

        self.server = server
        self.client = client

    def run(self):
        self.listen()

    def listen(self):
        try:
            while self.client.connected:
                data = self.client.connection.recv(self.server.BUFFER_SIZE)

                if data:
                    message = pickle.loads(data)
                    self.handle(message)
        except (ConnectionAbortedError, ConnectionResetError) as e:
            # disconnection from either sides
            pass
        except Exception as e:
            print("exception: '%s' in %s's connection, terminating connection"
                % (e, self.client.username))

        self.client.disconnect()

    def send(self, message):
        data = pickle.dumps(message, pickle.HIGHEST_PROTOCOL)
        self.client.connection.sendall(data)
        print("sent %d bytes to %s" % (len(data), self.client.username))

    def handle(self, message):
        print("message received from %s" % self.client.username)

        if not isinstance(message, msg.MsgRoot):
            raise RuntimeError(
                "invalid message from %s" % self.client.username)

        if message.messageType == msg.NONE:
            self.none_msg(message)
        elif message.messageType == msg.SIGN_IN:
            self.signin_msg(message)
        elif message.messageType == msg.SIGN_UP:
            self.signon_msg(message)

        print("finished handle of %s's message" % self.client.username)

    # message handlers
    def none_msg(self, message):
        print("none")
        self.send(msg.MsgRoot())

    def signin_msg(self, message):
        print("sign_in")
        self.send(msg_on_signin.MsgOnSignIn())

    def signon_msg(self, message):
        print("sign_on")
        self.send(msg_on_signon.MsgOnSignOn())
