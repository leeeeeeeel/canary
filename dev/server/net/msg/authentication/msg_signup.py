""" """

from net.msg import msg

class MsgSignUp(msg.MsgRoot):
    def __init__(self):
        self.messageType = msg.SIGN_UP
