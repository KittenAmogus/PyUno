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

		elif self.value in (
			CardCodes.BLOCK,
			CardCodes.REVERSE,
			CardCodes.PLUS_2
		):
			return CardCodes.ACT

		return CardCodes.WIL
	
	@property
	def code( self ):
		return self.color + self.value


def cardFromCode( code ):
	return Card( code // 0x10 * 0x10, code % 0x10 )

