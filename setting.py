from codes import ALL_CARDS

# In original UNO there is 7 card per player at start
START_CARD_COUNT	=	7

# Maximum players can play with at least 1 ex. card ( table card )
MAX_PLAYES			=	(len( ALL_CARDS ) - 1 ) // START_CARD_COUNT

# Server address and port
ADDRESS	=	"0.0.0.0"
PORT	=	0x7777  # beutiful in code, but default in real :)
# 0x because 7777 may be taken by Terraria server and some other servers

