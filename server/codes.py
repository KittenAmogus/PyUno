class ServerCodes:	# To player
	CONNECTED		=	0x00	# PLAYER_ID
	FAILED			=	0x01	# FAIL CODE

	PLAYER_JOINED	=	0x02	# PLAYER_ID
	PLAYER_LEFT		=	0x03	# PLAYER_ID

	PLAYER_TURN		=	0x04	# PLAYER_ID
	PLAYER_DRAWED	=	0x05	# CARD_COUNT
	PLAYER_PLACED	=	0x06	# CARD_CODE

	FORCE_DRAW		=	0x07	# CARD_CODE


class PlayerCodes:	# From player
	DRAW_CARD		=	0x00	# 00
	PLACE_CARDS		=	0x01	# CARDS_COUNT

	LEAVE_GAME		=	0x02	# 00


class CardCodes:
	# -- Colors --
	WILD	=	0x00
	RED		=	0x10
	GREEN	=	0x20
	YELLOW	=	0x30
	BLUE	=	0x40
	# MAGENTA	=	0x50
	# CYAN		=	0x60
	COLORS	=	[ RED, GREEN, YELLOW, BLUE ]
	# Wild color only exist in hand for Wild cards,
	# you must specify color before placing Wild card

	# -- Values --
	# Numbers
	NUMBERS		=	list(range( 0, 10 ))  # 0 - 9

	# Act
	REVERSE		=	0x0A
	BLOCK		=	0x0B
	PLUS_2		=	0x0C
	ACT_CARDS	=	[ REVERSE, BLOCK, PLUS_2 ]

	# Wild
	FORTUNE		=	0x0D
	WILD_PLUS_4	=	0x0E
	# SWAP_HANDS	=	0x0F
	WILD_CARDS	=	[ FORTUNE, WILD_PLUS_4 ]

	# # -- Types --
	# TYPE_NUMBER	=	0x00
	# TYPE_ACT	=	0x01
	# TYPE_WILD	=	0x02
	# # Types are only for drawing (and maybe filters)

