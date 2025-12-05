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

	PLAYER_NAME		=	0x07
	YOUR_CARD		=	0x08

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
	NUM_1	=	0x01
	NUM_2	=	0x02
	NUM_3	=	0x03
	NUM_4	=	0x04
	NUM_5	=	0x05
	NUM_6	=	0x06
	NUM_7	=	0x07
	NUM_8	=	0x08
	NUM_9	=	0x09
	NUM_10	=	0x00

	# Action
	BLOCK	=	0x0A
	REVERSE	=	0x0B
	PLUS_2	=	0x0C

	# Wild
	FORTUNE	=	0x0D
	PLUS_4	=	0x0E

	# Custom value
	CUSTOM	=	0x0F

