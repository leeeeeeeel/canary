""" """

from net.msg import msg

class MsgOnSignUp(msg.MsgRoot):
    def __init__(self):
        self.messageType = msg.ON_SIGN_UP
