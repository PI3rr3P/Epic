class Piece:
	def __init__(self, pos, color):
		self.pos = pos
		self.type = "abstract"
		self.color = "white"

class King(Piece):
	def __init__(self, pos, color):
		super().__init__(pos, color)
		self.type = "King"

