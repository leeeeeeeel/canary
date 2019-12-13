""" Canary server """

import net.server as s
import ui.input_handler as i

def main():
    server = s.Server()
    server.listen_async()
    i.listen(server)

if __name__ == "__main__":
    main()
