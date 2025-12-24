from codes import CardCodes


class Card:
	def __init__( self, color, value ):
		self.color	=	color
		self.value	=	value
	
	def __str__( self ):
		return f"({self.color} {self.value})"

	@property
	def type( self ):
		if self.value in CardCodes.NUMBERS:
			return CardCodes.NUM

		elif self.value in CardCodes.ACT_CARDS:
			return CardCodes.ACT

		elif self.value in CardCodes.WILD_CARDS:
			return CardCodes.WIL
		
		raise TypeError( "Invalid card value" )
	
	@property
	def code( self ):
		return self.color + self.value


def cardFromCode( code ):
	return Card( code // 0x10 * 0x10, code % 0x10 )

