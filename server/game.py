import random

import codes
from setting import *
from card import Card
from player import Player
from server import Server


class Game( Server ):
	def __init__( self ):
		self.players	=	[]
		self.playerTurn	=	0
		
		self.tableCard	=	None
		self.deck		=	[]
		self.discard	=	[]

		self.turnQueue	=	1  # -1 -- counterclockwise
		self.game		=	False
	
	# --- Game init ---

	def _startGame( self ):
		self._onGameStart()
		self._createDeck()
		self._shuffleDeck()
		self._setTableCard()
		self.game	=	True
	
	def _stopGame( self ):
		self._onGameEnd()
	
	def _createDeck( self ):
		pass
	
	def _setTableCard( self ):
		self._onSetTableCard()
	
	# --- Game process ---
	
	def _shuffleDeck( self ):
		pass
	
	def _getCard( self ):
		pass
	
	def _playerTurn( self ):
		pass
	
	# --- Player ---

	def _areAllPlayersReady( self ):
		pass

	def _drawCard( self ):
		pass
	
	def _placeCard( self ):
		pass
	
	def _waitForPlayers( self ):
		while( len( self.players ) < MAX_PLAYERS ):
			sock	=	self._waitForPlayer()
			
			if ( not sock or sock is None ):
				continue

			player	=	Player( sock, len( self.players ))
			if ( not self._onPlayerJoined( player ) ):
				self._onPlayerLeft( player )
				continue

			self.players.append( player )
			if ( self._areAllPlayersReady() ):
				break

		return True
	
	# --- Main ---

	def start( self ):
		if ( not self._createServer() ):
			return
		
		if ( not self._waitForPlayers() ):
			return

		self._startGame()

		while ( self.game ):
			self._playerTurn()

		self._stopGame()


def _main():
	game = Game()
	game.start()


if __name__ == "__main__":
	_main()
