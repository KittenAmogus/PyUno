class Card:
	def __init__(self, color, value):
		self.color	=	color
		self.value	=	value
		
	@property
	def type(self):
		if self.value in "0123456789":
			return "num"
		
		elif self.value in (
			"block",
			"reverse",
			"plus2"
		):
			retun "act"

		return "wil"

	def __str__(self):
		pass

