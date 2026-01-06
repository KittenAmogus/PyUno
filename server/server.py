import logging
import socket
import json

from codes import CardCodes, PlayerCodes, ServerCodes
from card import Card


LOG_LEVEL		=	logging.DEBUG	# logging.INFO
# LOG_PATH		=	"./Logs"

# from os import mkdir, path
# from datetime import datetime

# if ( not path.exists( LOG_PATH ) ):
# 	mkdir( LOG_PATH )

# # 'DD.MM.YYYY HH:MM:SS.MS' to 'HH:MM:SS'
# time = str( datetime.now() ).split()[ 1 ].split( '.' )[ 0 ]
# LOG_FILE		=	f"{ LOG_PATH.removesuffix( '/' ) }/" f"server-{ time }.log"
LOG_FILE	=	"log-server.log"

# del mkdir, datetime

LOG_FORMAT		=	'[%(levelname)s] (%(asctime)s) %(message)s'

logger			=	logging.getLogger( __name__)
logging.basicConfig( level=LOG_LEVEL, filename=LOG_FILE, format=LOG_FORMAT )
logger.info( "\n\r--- New Session ---\n\r" )


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

	def _createServer( self ):
		self.socket	=	socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		self.socket.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
		logger.debug( "Created server" )

		try:
			self.socket.bind(( self.host, self.port ))
			logger.debug( "Server bind success" )
			self.socket.listen( self.max_clients )
			logger.debug( "Server listen success" )
			logger.info( f"Server listen on { self.host }:{ self.port }" )

		except OSError as e:
			logger.error( f"Cannot bind/listen server: { e }" )
			return False

	def _stopServer( self ):
		self.socket.detach()
		self.socket.close()
		logger.info( "Closed server" )
	
	# --- Client ---

	def _onPlayerJoined( self ):
		pass
	
	def _onPlayerLeft( self ):
		pass
	
	def _onPlayerTurn( self ):
		pass
	
	def _waitPlayer( self ):
		try:
			sock, addr = self.socket.accept()
			logger.info( f"User connected: { addr[ 0 ] }:{ addr[ 1 ] }" )
			return sock

		except OSError as e:
			logger.error( f"Server connecting error: { e }" )
			raise e

		except ConnectionError:
			logger.error( f"User connection error: { e }" )
			return None

		return None
	
	# --- Game ---

	def _onPlaceCard( self ):
		pass
	
	def _onDrawCard( self ):
		pass


class Game( Server ):
	def __init__( self ):
		super().__init__()
	
	# --- Server ---

	def _startGame( self ):
		self._createServer()
	
	def _stopGame( self ):
		self._stopServer()
	
	# --- Players ---

	def _waitForPlayers( self ):
		while ( len( self.players ) < self.max_clients ):
			sock	=	self._waitPlayer()
			if ( sock is None ):
				continue

			self.players.append( sock )

	# --- Start ---
	def start( self ):
		self._startGame()

		try:
			self._waitForPlayers()
	
		except KeyboardInterrupt:
			logger.debug( "Received Ctrl+C" )

		finally:
			self._stopGame()


def main():
	Game().start()

if __name__ == "__main__":
	main()

