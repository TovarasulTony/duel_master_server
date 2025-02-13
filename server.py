import configparser
import socket

class Server:
    def __init__(self):
        # Config
        self.config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        self.config.read('config/config.ini')

        # Socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.config.get("server", "ip_address"), self.config.getint("server", "server_port")))
        self.socket.listen(2)
        
        self.main_loop()

    def main_loop(self):
        print("[Server] Open for connections")
        while True:
            conn, addr = self.socket.accept()
            print("[Server] New Client: " + str(addr))
            exit()
            new_client = Client(self, self.command_handler.execute_command)
            new_client.setup_client(conn, addr)
            print("[Server] New Client: " + str(addr))
        conn.close()
        self.socket.close()

    def add_player(self, room, player):
        self.room_list[room].append(player)


server = Server()
print(server.config["user"]["min_user"])