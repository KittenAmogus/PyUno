import socket
import json


from codes import CardCodes, PlayerCodes, ServerCodes
from card import Card


class LogLevels:
	ERROR		=	0
	EXCEPTION	=	1
	INFO		=	2
	DEBUG		=	3

	@staticmethod
	def stringFromLevel( lvl ):
		match ( lvl ):
			case 0:	return "ERROR"
			case 1:	return "EXCEPTION"
			case 2:	return "INFO"
			case 3:	return "DEBUG"
			case _:	return "-"


LOG_LEVEL_PRINT	= LogLevels.INFO
LOG_LEVEL_FILE	= LogLevels.DEBUG


def log( level, msg ):
	match ( level ):
		case ( LogLevels.ERROR ):		color = "5;101;30"
		case ( LogLevels.EXCEPTION ):	color = "91"
		case ( LogLevels.INFO ):		color = "93"
		# case ( "debug" ):		color = "0"
		case _:					color = "0"
	
	if ( LOG_LEVEL_PRINT >= level ):
		print( f"\x1b[{ color }m[{ LogLevels.stringFromLevel(level) }]:",
				msg, "\x1b[0m" )
	if ( LOG_LEVEL_FILE >= level ):
		...  # save to file


class Server:
	def __init__( self ):
		try:
			with open( "setting.json", "r" ) as setting_file:
				setting	=	json.load( setting_file )
		except FileNotFoundError:
			setting		=	{}

		self.host			=	setting.get( "host", "localhost"  )
		self.max_clients	=	setting.get( "max-clients", 6 )
		self.port			=	setting.get( "port", 7777 )

		self.players		=	[]

		self.socket			=	None
	
	# --- Server ---

	def createServer( self ):
		self.socket	=	socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		self.socket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )

		try:
			self.socket.bind(( self.host, self.port ))
			self.socket.listen( self.max_clients )
			log( LogLevels.INFO, f"Listen on: { self.host }:{ self.port }" )

		except OSError as e:
			log( LogLevels.ERROR, f"Cannot bind/listen: { e }" )
			return False

	def stopServer( self ):
		self.socket.detach()
		self.socket.close()
		log( LogLevels.INFO, "Server closed" )
	
	# --- Client ---

	def playerJoined( self ):
		pass
	
	def playerLeft( self ):
		pass
	
	def playerTurn( self ):
		pass
	
	# --- Game ---

	def placeCard( self ):
		pass
	
	def drawCard( self ):
		pass
	

def main():
	...

if __name__ == "__main__":
	main()

