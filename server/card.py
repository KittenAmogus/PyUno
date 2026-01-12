class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value
        self.code = color + value  # For sending

    def __str__(self):
        return f"\033[9{self.color}m" + f"({self.value})"

    def __repr__(self):
        return f"Card({self.color}, {self.value})"
