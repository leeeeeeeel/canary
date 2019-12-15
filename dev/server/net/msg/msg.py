""" """

NONE = 0

SIGN_IN = 1
ON_SIGN_IN = 2
SIGN_UP = 3
ON_SIGN_UP = 4

class MsgRoot:
    def __init__(self):
        self.messageType = NONE
