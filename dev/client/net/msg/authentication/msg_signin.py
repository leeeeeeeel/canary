""" """

from net.msg import msg

class MsgSignIn(msg.MsgRoot):
    def __init__(self):
        self.messageType = msg.SIGN_IN
