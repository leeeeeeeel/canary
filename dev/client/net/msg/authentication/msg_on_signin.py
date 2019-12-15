""" """

from net.msg import msg

class MsgOnSignIn(msg.MsgRoot):
    def __init__(self):
        self.messageType = msg.ON_SIGN_IN
