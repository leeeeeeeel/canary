""" """

# TODO
def listen(server):
    try:
        while server.running:
            args = input().split(" ")
            handle(server, args)
    except (KeyboardInterrupt, SystemExit):
        server.shut()

def handle(server, args):
    pass

def help(args):
    pass

def quit(server, args):
    server.shut()

def restart(args):
    pass

def status(args):
    pass

def log(args):
    pass
