class PlayerCodes:
	# Code Value
	LEAVE_GAME		=	0x00  # 00

	PLACE_CARD		=	0x01  # CARD CODE
	PLACE_MULTIPLE	=	0x02  # COUNT
	DRAW_CARD		=	0x03  # 00


class ServerCodes:
	# Code Value
	GAME_STARTED	=	0x00  # 00
	GAME_ENDED		=	0x01  # 00

	PLACED_CARD		=	0x02  # CARD CODE
	DRAWED_CARD		=	0x03  # PLAYER CODE
	FORCE_DRAW		=	0x04  # CARD COUNT

	LEFT_GAME		=	0x05  # PLAYER CODE
	JOINED_GAME		=	0x06  # PLAYER CODE

	PLAYER_NAME		=	0x07  # PLAYER CODE

	CONNECTED		=	0x0A  # 00
	FAILED_CONNECT	=	0x0B  # 00

class CardCodes:
	# Color Value
	
	# --- Color ---

	WILD	=	0x00

	RED		=	0x01
	GREEN	=	0x02
	YELLOW	=	0x03
	BLUE	=	0x04
	
	# # Add more colors if u want
	# PINK	=	0x05
	# CYAN	=	0x06

	# --- Value ---
	
	# Number
	NUMBERS = (i % 11 for i in range(1, 11))

	# Action
	BLOCK	=	0x0A
	REVERSE	=	0x0B
	PLUS_2	=	0x0C

	# Wild
	FORTUNE	=	0x0D
	PLUS_4	=	0x0E

	# Custom value
	CUSTOM	=	0x0F

	@staticmethod
	def createValues(col, val):

		match (val):
			case "block":
				value = BLOCK
			case "reverse":
				value =  REVERSE
			case "plus2":
				value =  PLUS_2

			case "fortune":
				value =  FORTUNE
			case "plus4":
				value =  PLUS_4

			case _:
				if 0 <= val < 10:
					value = NUMBERS[ val ]
				else:
					value = CUSTOM

		match (col):
			case "red":
				return RED, value
			case "green":
				return GREEN, value
			case "yellow":
				return YELLOW, value
			case "blue":
				return BLUE, value

			# case "cyan":
			# 	return CYAN, value
			# case "pink":
			# 	return PINK, value

			case _:
				return WILD, value

