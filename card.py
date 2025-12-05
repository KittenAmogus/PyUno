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
			return "act"

		return "wil"

	def __str__(self):
		match (self.color):
			case "red":		color = 91
			case "green":	color = 92
			case "yellow":	color = 93
			case "blue":	color = 94
			case "pink":	color = 95
			case "cyan":	color = 96
			
			case _:			color = 0

		return f"\x1b[{color}m" f"({self.value})"

