from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

from codes import PlayerCodes, ServerCodes, CardCodes


class Player:
	def __init__(self, id_):
		self.id		=	id_
		self.socket	=	None
		self.hand	=	[]
	
	def _recvData(self, size):
		pass
	
	def sendData(self, *data):
		pass
	
	def playerTurn(self):
		pass

