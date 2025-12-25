from socket import AF_INET, SOCK_STREAM
from socket import SOL_SOCKET, SO_REUSEADDR
from socket import socket

from setting import ADDRESS, PORT, MAX_PLAYES
from codes import ServerCodes


class Server:
	def __init__( self ):
		self.sock		=	None
		self.players	=	[]
	
	# --- Server ---

	def createServer( self ):
		self.sock	=	socket( AF_INET, SOCK_STREAM )
		self.sock.setsockopt( SOL_SOCKET, SO_REUSEADDR, 1 )

		self.sock.bind(( ADDRESS, PORT ))
		self.sock.listen( MAX_PLAYES )
	
	def closeServer( self ):
		self.sock.detach()
		self.sock.close()
	
	def sendAll( self, *data ):
		# byte_data	=	bytearray( data )
		for player in self.players:
			player.sendData( *data )
	
	# --- Game ---

	def gameStart( self ):
		pass
	
	def gameEnd( self ):
		pass
	
	def placeCard( self ):
		pass
	
	def drawCard( self, player_id, card_code ):
		pass
	
	# --- Player ---

	def playerJoined( self, player ):
		self.players.append( player )
		player.sendData( ServerCodes.CONNECTED, player.id )
		self.sendAll( ServerCodes.PLAYER_JOINED, player.id  )
	
	def playerLeft( self ):
		pass
	
	def waitForPlayer( self ):
		sock, addr	=	self.sock.accept()
		return sock, addr

