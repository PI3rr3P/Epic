class Piece:
	def __init__(self, pos, color):
		self.pos = pos
		self.type = "abstract"
		self.color = "white"

	def possibleSquare(self):
		pass

class King(Piece):
	def __init__(self, pos, color):
		super().__init__(pos, color)
		self.type = "King"

	def possibeSquare(self):
		possible = []
		for i in range(-1:1):
			for j in range(-1:1):
				if i == 0 or j == 0:
					possible.append( (self.pos[0] + i, self.pos[1] + j) )
		return possible

