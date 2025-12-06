from card import Card

# later in config
ADDR		=	"localhost"
PORT		=	4444
MAX_CLIENTS	=	3
START_CARDS	=	7

# Deck
COLORS = (
			"red",
			"green",
			"yellow",
			"blue"
			# ,"pink", "cyan"
			# Add more colors if u want
			)

NUMBERS		=	range(10)
ACT_CARDS	=	("block", "reverse", "plus2")
WILD_CARDS	=	("fortune", "plus4")

FULL_DECK	= [
	Card(color, value)
	for color in COLORS
	for value in ACT_CARDS + tuple(NUMBERS)
	for _ in range(2)
] + [Card("wil", value) for value in WILD_CARDS for _ in range(4)]

