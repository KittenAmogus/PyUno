import socket

import codes


HOST		=	"localhost"
PORT		=	7777
MAX_PLAYERS	=	6	# Can be up to 17 if start hand contains 7 cards


class Server:
	def __init__( self ):
		self.socket		=	None
		self.user_socks	=	[]
	
	# --- Server ---

	def _createServer( self ) -> bool:
		self.socket		=	socket.socket(
			socket.AF_INET, socket.SOCK_STREAM
		)
		self.socket.setsockopt(
			socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
			# If code breaks, new socket can bind on this addr
		)

		try:
			self.socket.bind(( HOST, PORT ))
			self.socket.listen( MAX_PLAYERS )

			return True

		except OSError as err:
			print( "\x1b[101;30;5m" + str( err ) + "\x1b[0m" )
			raise err

		return False
	
	def _closeServer( self ) -> None:
		self.socket.detach()
		self.socket.close()
		self.socket	=	None
	
	# --- Game ---

	def _onSetTableCard( self ):
		pass
	
	def _onGameStart( self ):
		pass
	
	def _onGameEnd( self ):
		self._closeServer()
	
	def _onCardDraw( self ):
		pass
	
	def _onCardPlace( self ):
		pass
	
	# --- Player ---
	
	def _onPlayerJoined( self ):
		pass
	
	def _onPlayerLeft( self ):
		pass
	
	def _waitForPlayer( self ):
		pass

