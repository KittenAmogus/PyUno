from socket import AF_INET, SOCK_STREAM
from socket import SOL_SOCKET, SO_REUSEADDR
from socket import socket

from setting import ADDRESS, PORT, MAX_PLAYES


class Server:
	def __init__( self ):
		self.sock	=	None
	
	# --- Server ---

	def createServer( self ):
		self.sock	=	socket( AF_INET, SOCK_STREAM )
		self.sock.setsockopt( SOL_SOCKET, SO_REUSEADDR, 1 )

		self.sock.bind(( ADDRESS, PORT ))
		self.sock.listen( MAX_PLAYES )
	
	def closeServer( self ):
		pass
	
	# --- Game ---

	def gameStart( self ):
		pass
	
	def gameEnd( self ):
		pass
	
	def placeCard( self ):
		pass
	
	def drawCard( self ):
		pass
	
	# --- Player ---

	def playerJoined( self, player_id ):
		pass
	
	def playerLeft( self ):
		pass
	
	def waitForPlayer( self ):
		sock, addr	=	self.sock.accept()
		return sock, addr

