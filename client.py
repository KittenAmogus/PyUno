from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from socket import socket

from codes import PlayerCodes, ServerCodes, CardCodes
from card import Card
from setting import ADDR, PORT


class Client:
	def __init__(self):
		# Client
		self.sock = None
		self.id = None

		# Game
		self.hand = []
		self.tableCard = None
	
	# --- Client Actions ---
	
	def _createClient(self):
		try:
			self.sock = socket(AF_INET, SOCK_STREAM)
			self.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

			self.sock.connect((ADDR, PORT))
		
		except Exception as e:
			print(f"Error creating client: {e}")
			return False

		return True
	
	def _register(self):
		

