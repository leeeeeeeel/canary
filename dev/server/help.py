""" """

from datetime import datetime

def anon_username():
    return "anon" +  str(datetime.now().microsecond)
