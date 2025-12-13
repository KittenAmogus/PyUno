class ServerCodes:
	CONNECTED			=	0x00  # 00
	FAILED_TO_CONNECT	=	0x01  # 00

	PLAYER_JOINED		=	0x02  # PLAYER ID
	PLAYER_LEFT			=	0x03  # PLAYER ID

	GAME_STARTED		=	0x03  # 00
	GAME_ENDED			=	0x04  # 00

	PLAYER_TURN			=	0x05  # PLAYER_ID
	DRAWED_CARD			=	0x06  # PLAYER_ID
	PLACED_CARD			=	0x07  # PLAYER_ID

	NEW_TABLE_CARD		=	0x08  # CARD CODE

	FORCE_DRAW			=	0x09  # CARD CODE


class PlayerCodes:
	LEAVE_GAME			=	0x00  # 00
	
	DRAW_CARD			=	0x01  # 00
	PLACE_CARD			=	0x02  # CARD ID


class CardCodes:

	# VALUES
	NUMBERS = tuple(
		i for i in range( 10 )
	)

	BLOCK		=	0x0A
	REVERSE		=	0x0B
	PLUS_2		=	0x0C

	FORTUNE		=	0x0D
	WILD_PLUS_4	=	0x0E

	CUSTOM_CARD	=	0x0F  # like 'swap hands'

	# COLORS
	RED			=	0x01
	GREEN		=	0x02
	YELLOW		=	0x03
	BLUE		=	0x04

