from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

from codes import PlayerCodes, ServerCodes, CardCodes


class Player:
	def __init__(self, sock, id_):
		self.id		=	id_
		self.socket	=	sock
		self.hand	=	[]
	
	def _recvData(self, size):
		return self.socket.recv(size)
	
	def _drawCard(self, card):
		self.hand.append(card)
		self.sendDat(ServerCodes.DRAW_CARD,
		CardCodes.createValues(card.color,
		card.value))

	def sendData(self, *data):
		self.socket.sendall(bytearray(data))
	
	def playerTurn(self):
		return self._recvData(2)

