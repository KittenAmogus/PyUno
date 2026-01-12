import codes


class Player:
    def __init__(self, socket, id_):
        self.socket = socket
        self.id = id_

        self.hand = []
        self.ready = False
        # self.name    =    None

    def drawCard(self, card):
        if card.code != 0x0F:
            self.hand.append(card)

    def sendData(self, *data):
        self.socket.sendall(bytearray(data))

    def recvData(self, dataLength=2):
        return self.socket.recv(dataLength)
