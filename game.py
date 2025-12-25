import logging
import random

from setting import *
from player import Player
from server import Server
from card import cardFromCode
from codes import ServerCodes, PlayerCodes, CardCodes
from codes import ALL_CARDS


class Game:
	def __init__( self ):
		# Game
		self.players	=	[]
		self.playerTurn	=	0
		self.turnOrder	=	1

		# Deck
		self.deck		=	[]
		self.garbage	=	[]
		self.tableCard	=	None

		# Server
		self.server		=	None

		# Logger
		self.logger		=	logging.getLogger( __name__ )
		logging.basicConfig(
			# filename="log-DATE.log",
			level=logging.INFO,
			format="%(levelname)s\t%(message)s"
		)
	
	# --- Server ---

	def _createServer( self ):
		self.server		=	Server()
		self.server.createServer()
		self.logger.info( f"Created server: { ADDRESS }:{ PORT }" )
	
	def _closeServer( self ):
		self.server.closeServer()
		self.logger.info( "Closed server" )
	
	def _playerJoined( self, sock, addr ):
		self.logger.info( f"Joined player, { addr }" )
		player	=	Player( sock, len( self.players ) )
		self.players.append( player )
		self.server.playerJoined( player )
	
	def _playerLeft( self ):
		self.server.playerLeft()
	
	# --- Deck ---

	def _createDeck( self ):
		self.deck		=	ALL_CARDS.copy()
		self.garbage.clear()
	
	def _shuffleDeck( self ):
		for card in self.garbage:
			self.deck.append( card )
		self.garbage.clear()
		random.shuffle( self.deck )
	
	def _placeCard( self ):
		self.server.placeCard()
	
	def _getCard( self ):
		if len( self.deck ) < 1:
			self._shuffleDeck()

		card = self.deck[ -1 ]
		self.deck.pop( -1 )
		return card
	
	def _drawCard( self, player ):
		card	=	self._getCard()
		player.drawCard( card )
		self.server.drawCard( player.id, card.code )

	# --- Game ---

	def _gameStart( self ):
		for c in range( START_CARD_COUNT ):
			for player in self.players:
				self._drawCard( player )
			self.logger.info( f"Players drawed card: { c }" )

	def _gameEnd( self ):
		pass
	
	def _playerTurn( self ):
		pass

	def _gameTurn( self ):
		pass
	
	def _waitForPlayers( self ):
		while ( len( self.players ) ) < MAX_PLAYES:
			conn		=	self.server.waitForPlayer()

			# If connection error
			if not conn:
				self.logger.warning( f"Error connecting: { conn }" )
				continue

			sock, addr	=	conn
			self._playerJoined( sock, addr )

			# TODO replace with 'ready'
			if input("start> ") == "y":
				break
	
	# --- Main ---

	def start( self ):
		self._createServer()
		self._createDeck()

		self._waitForPlayers()

		self._gameStart()
		self._gameEnd()
		self._closeServer()


if __name__ == "__main__":
	Game().start()

