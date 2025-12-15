import random

from server import Server
from card import Card, cardFromCode
from codes import ServerCodes, PlayerCodes, CardCodes


class Game:
	def __init__( self ):
		# Game
		self.players	=	[]
		self.playerTurn	=	0
		self.turnOrder	=	1

		# Deck
		self.deck		=	[]
		self.tableCard	=	None

		# Server
		self.server		=	None
	
	# --- Server ---

	def _createServer( self ):
		pass
	
	def _closeServer( self ):
		pass
	
	def _playerJoined( self ):
		pass
	
	def _playerLeft( self ):
		pass
	
	# --- Deck ---

	def _createDeck( self ):
		pass
	
	def _shuffleDeck( self ):
		pass
	
	def _placeCard( self ):
		pass
	
	def _getCard( self ):
		pass

	# --- Game ---

	def _gameStart( self ):
		pass
	
	def _gameEnd( self ):
		pass
	
	def _playerTurn( self ):
		pass

	def _gameTurn( self ):
		pass
	
	# --- Main ---

	def start( self ):
		pass


if __name__ == "__main__":
	Game().start()

