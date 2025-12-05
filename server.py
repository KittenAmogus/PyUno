from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from random import shuffle, seed

from codes import PlayerCodes, ServerCodes, CardCodes
from card import Card
from player import Player


# later in config
ADDR		=	"localhost"
PORT		=	4444
MAX_CLIENTS	=	6

# Deck
COLORS = (
			"red",
			"green",
			"yellow",
			"blue"
			# ,"pink", "cyan"
			# Add more colors if u want
			)

NUMBERS		=	range(10)
ACT_CARDS	=	("block", "reverse", "plus2")
WILD_CARDS	=	("fortune", "plus4")

FULL_DECK	= [
	Card(color, value)
	for color in COLORS
	for value in ACT_CARDS + tuple(NUMBERS)
	for _ in range(2)
] + [Card("wil", value) for value in WILD_CARDS for _ in range(4)]


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
		pass
	
	def _createDeck(self):
		print("Creating deck... ", end="")
		self.garbage.clear()
		self.deck = FULL_DECK
		shuffle(self.deck)
		print("done")

	# --- Server Actions ---

	def _sendall(self, *data):
		for player in self.players:
			player.sendData(*data)

	def _createServer(self):
		self.socket	=	socket(AF_INET, SOCK_STREAM)
		self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

		self.socket.bind((ADDR, PORT))
		self.socket.listen(MAX_CLIENTS)

		print(f"Server created {ADDR}:{PORT}")
	
	def _closeServer(self):
		self.socket.detach()
		self.socket.close()
		print("Stopped socket")

	def _playerJoined(self, sock):
		player = Player(sock, len(self.players))
		if not self._registerPlayer(player):
			print("Player not registered!")
			return False

		self.players.append(player)
		return True
	
	def _playerLeft(self):
		pass
	
	def _registerPlayer(self, player):
		return True
	
	def _waitForPlayers(self):
		while len(self.players) < MAX_CLIENTS:
			usr, addr = self.socket.accept()
			usr.sendall(bytearray((
				ServerCodes.CONNECTED, 0x00
			)))
			if not self._playerJoined(usr):
				continue

			match input(f"({len(self.players)}/{MAX_CLIENTS}) players |"
			" S - start game, Q - quit game > ").lower():
				case "s":
					return True

				case "q":
					return False

	# --- Game Actions ---

	def _gameStart(self):
		self._createDeck()
		self.game		= True
		self.playerTurn	= 0

	def _gameEnd(self):
		print("Game stopped")
		self.game	= False
	
	def _gameTurn(self):
		player = self.players[ self.playerTurn ]
		self._sendall(ServerCodes.JOINED_GAME, 0)
		self.playerTurn += 1

		code, value = player.playerTurn()

		return False
	
	def _gameLoop(self):
		while self.game:
			if self._gameTurn():
				self._gameEnd()
				break

	# --- Start Actions ---
	
	def startGame(self):
		self._createServer()
		self._waitForPlayers()
		
		self._initGame()
		self._gameStart()

		self._gameLoop()
		self._closeServer()

def _main():
	Game().startGame()


if __name__ == "__main__":
	_main()

