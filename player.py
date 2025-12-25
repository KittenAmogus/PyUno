class Player:
	def __init__( self, sock, id_ ):
		# Server
		self.sock	=	sock
		self.id		=	id_

		# Game
		self.ready	=	False
		self.name	=	None
		self.hand	=	[]
	
	def placeCard( self, cardId ):
		card		=	self.hand[ cardId ]
		self.hand.pop( cardId )
		return card
	
	def drawCard( self, card ):
		self.hand.append( card )
	
	def sendData( self, *data ):
		self.sock.sendall( bytearray( data ) )

