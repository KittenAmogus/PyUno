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
	# Values

	BLOCK		=	0x0A
	REVERSE		=	0x0B
	PLUS_2		=	0x0C

	FORTUNE		=	0x0D
	WILD_PLUS_4	=	0x0E

	CUSTOM_CARD	=	0x0F  # like 'swap hands'

	# COLORS$a
	WILD		=	0x00
	RED			=	0x10
	GREEN		=	0x20
	YELLOW		=	0x30
	BLUE		=	0x40

	# TYPES
	NUM			=	0x01
	ACT			=	0x02
	WIL			=	0x03

	# Generators
	# FIXME fix these stupid errors with numbers not defined
	COLORS		=	RED, GREEN, YELLOW, BLUE

	NUMBERS 	=	list(
		i for i in range( 10 )
	)

	ACT_VALUES	=	[ BLOCK, REVERSE, PLUS_2 ]

	WILD_VALUES	=	[ FORTUNE, WILD_PLUS_4 ]


from card import Card

NUMBER_CARDS	=	[
	Card( col, val )
	for col in CardCodes.COLORS
	for val in CardCodes.NUMBERS
	for _ in range( 2 )
]

ACT_CARDS	=	[
	Card( col, val )
	for col in CardCodes.COLORS
	for val in CardCodes.ACT_VALUES
	for _ in range( 2 )
]

WILD_CARDS	=	[
	Card( CardCodes.WILD, val )
	for val in CardCodes.WILD_VALUES
	for _ in range( 4 )
]

ALL_CARDS	=	NUMBER_CARDS + ACT_CARDS + WILD_CARDS
