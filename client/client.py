import socket

from card import Card
import codes


class Client:
    def __init__(self):
        self.host = "localhost"
        self.port = 7777

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.hand = []
        self.tableCard = None

        self.otherPlayers = []
        self.isReady = True

        self.playerTurnId = 0

        self.id = -1
        self.name = "\0"

    # --- Server ---Card
    def connectToServer(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.connect((self.host, self.port))

        try:
            self.socket.settimeout(5)
            data = bytearray(self.socket.recv(2))
            if len(data) != 2:
                raise IndexError("Server sent invalid connection code")

            if data[0] != codes.ServerCodes.CONNECTED:
                #                       Transofm 0xNN to 'NN'
                print(
                    f"Server error[ {hex(data[1]).split('x')[1]} ], try again later..."
                )
                return False

            self.id = data[1]

            print(f"Connected, ID: {self.id}")

        except TimeoutError or ConnectionError:
            print("Error connecting to server, try again later...")
            return False

        except OSError as e:
            print(
                "Cannot connect to server (Waiting probably won't help, try fixing code!)"
            )
            raise e

    def leaveGame(self):
        pass

    # --- Game ---

    # --- Run ---
    def run(self):
        pass
