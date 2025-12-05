from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

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
		self.tableCard	=	None
		self.playerTurn	=	0

		self.deck		=	[]
		self.garbage	=	[]
	
	# --- Init Actions ---

	def _initGame(self):
		pass
	
	def _createDeck(self):
		pass

	# --- Server Actions ---

	def _createServer(self):
		pass
	
	def _closeServer(self):
		pass
	
	def _playerJoined(self):
		pass
	
	def _playerLeft(self):
		pass
	
	def _registerPlayer(self):
		pass

	# --- Game Actions ---

	def _gameStart(self):
		pass
	
	def _gameEnd(self):
		pass
	
	def _gameTurn(self):
		pass
	
	def _gameLoop(self):
		pass

	# --- Start Actions ---
	
	def startGame(self):
		pass


def _main():
	pass


if __name__ == "__main__":
	_main()

