from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from random import shuffle, seed

from codes import PlayerCodes, ServerCodes, CardCodes
from card import Card
from player import Player
from setting import FULL_DECK, COLORS, ADDR, PORT, MAX_CLIENTS, START_CARDS


class Game:
	def __init__(self):
		# Server
		self.socket		=	None

		self.players	=	[]

		# Game
		self.game		= False

		self.tableCard	=	None
		self.playerTurn	=	0

		self.deck		=	[]
		self.garbage	=	[]
	
	# --- Init Actions ---

	def _initGame(self):
		self._createDeck()
	
	def _createDeck(self):
		print("Creating deck... ", end="")
		self.garbage.clear()
		self.deck = FULL_DECK.copy()
		shuffle(self.deck)
		print("done")

	# --- Server Actions ---

	def _sendall(self, *data):
		for player in self.players:
			player.sendData(*data)
	
	def _createServer(self):
		try:
			self.socket	=	socket(AF_INET, SOCK_STREAM)
			self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	
			self.socket.bind((ADDR, PORT))
			self.socket.listen(MAX_CLIENTS)

			print(f"Server created {ADDR}:{PORT}")

		except Exception as e:
			print(f"Error creating server: {e}")
			return False

		return True
	
	def _closeServer(self):
		self.socket.detach()
		self.socket.close()
		print("Stopped socket")
		return True

	def _playerJoined(self, sock):
		player = Player(sock, len(self.players))

		if not self._registerPlayer(player):
			print("Player not registered!")
			return False

		self.players.append(player)
		return True
	
	def _playerLeft(self, player):
		player.leaveGame()
		self.players.pop(player.id)
	
	def _registerPlayer(self, player):
		player.sendData(ServerCodes.CONNECTED, player.id)
		return True
	
	def _waitForPlayers(self):
		while len(self.players) < MAX_CLIENTS:
			usr, addr = self.socket.accept()
			if not self._playerJoined(usr):
				continue

	# --- Game Actions ---

	def _getCard(self):
		if len(self.deck) == 0:
			for i, g in self.garbage:
				self.deck.append(g)
				self.garbage.pop(i)  # not copy, but actual card

			shuffle(self.deck)

		card = self.deck[-1]
		self.deck.pop(-1)  # not copy, but actual card
		return card

	def _gameStart(self):
		self.game		= True
		self.playerTurn	= 0

	def _gameEnd(self):
		print("Game stopped")
		self.game	= False
	
	def _gameTurn(self):
		player = self.players[ self.playerTurn ]
		self._sendall(ServerCodes.PLAYER_TURN, player.id)
		self.playerTurn += 1

		code, value = player.playerTurn()
		print(hex(code), hex(value))

		return False
	
	def _gameLoop(self):
		while self.game:
			if self._gameTurn():
				self._gameEnd()
				break

	# --- Start Actions ---
	
	def startGame(self):
		self._createServer()
		self._initGame()
		self._waitForPlayers()
		
		self._gameStart()
		self._gameLoop()
		self._closeServer()

def _main():
	Game().startGame()


if __name__ == "__main__":
	_main()

