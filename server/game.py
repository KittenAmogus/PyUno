import random

import codes
from card import Card
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

	def _drawCard( self ):
		pass
	
	def _placeCard( self ):
		pass
	
	def _waitForPlayers( self ):
		pass
	
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
