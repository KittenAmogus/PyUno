import socket

import codes
import setting


class Server:
    def __init__(self):
        self.socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.user_socks = []

    # --- Server ---

    def _createServer(self) -> bool:
        self.socket.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1,
            # If code breaks, new socket can bind on this addr
        )

        try:
            self.socket.bind((setting.HOST, setting.PORT))
            self.socket.listen(setting.MAX_PLAYERS)

            return True

        except OSError as err:
            print("\x1b[101;30;5m" + str(err) + "\x1b[0m")
            raise err

    def _closeServer(self) -> None:
        self.socket.detach()
        self.socket.close()

    # --- Game ---

    def _onGameStart(self, tableCard):
        self._sendAll(codes.ServerCodes.GAME_START, tableCard.code)

    def _onGameEnd(self):
        self._closeServer()

    def _onCardDraw(self, player):
        for p in self.user_socks:
            p.sendall(bytearray((codes.ServerCodes.PLAYER_DRAWED, player.id)))

    def _onCardPlace(self, card):
        self._sendAll(codes.ServerCodes.PLAYER_PLACED, card.code)

    # --- Player ---

    def _sendAll(self, *data):
        data_ = bytearray(data)
        for p in self.user_socks:
            p.sendall(data_)

    def _onPlayerJoined(self, player):
        player.sendData(codes.ServerCodes.CONNECTED, player.id)
        self._sendAll(codes.ServerCodes.PLAYER_JOINED, player.id)
        return True
        # try-except will be later

    def _onPlayerLeft(self, player):
        self._sendAll(codes.ServerCodes.PLAYER_LEFT, player.id)

    def _onPlayerTurn(self, player):
        self._sendAll(codes.ServerCodes.PLAYER_TURN, player.id)

    def _onPlayerTurnEnd(self, player):
        self._sendAll(codes.ServerCodes.PLAYER_TURN_END, player.id)

    def _waitForPlayer(self):
        try:
            sock, _ = self.socket.accept()
            self.user_socks.append(sock)
            return sock

        except ConnectionError:  # idk what errors can apear here
            return None
