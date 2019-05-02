class Piece:
	def __init__(self, pos, color):
		self.pos = pos
		self.oldPos = []
		self.type = "abstract"
		self.color = "void"
		self.neverMove = True

	def possibleSquare(self, IMAX=None, JMAX=None):
		''' give possible position give a type of piece '''
		yield None

	def generatePath(self, pos):
		''' give the way the piece go, return a serie of position '''
		return []

	def __repr__(self):
		return {'type': self.type, 'color': self.color, 'pos':self.pos}

class King(Piece):
	def __init__(self, pos, color):
		super().__init__(pos, color)
		self.type = "king"

	def possibeSquare(self, IMAX=None, JMAX=None):
		for i in range(-1,1):
			for j in range(-1,1):
				if i == 0 or j == 0:
					yield (self.pos[0] + i, self.pos[1] + j)

	def generatePath(self, pos):
		return [pos]

class Pawn(Piece):
	def __init__(self, pos, color):
		super().__init__(pos, color)
		self.type = "pawn"

	def possibeSquare(self):
		possible = [ (0, 1), (1,1), (-1, -1)]
		for dpos in possible:
			yield (self.pos[0] + dpos[0], self.pos[1] + dpos[1])

	def generatePath(self, pos):
		return [pos]

class Knight(Piece):
	def __init__(self, pos, color):
		super().__init__(pos, color)
		self.type = "knight"

	def possibeSquare(self):
		possible = [ (-2, 1), (-2,-1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
		for dpos in possible:
			yield (self.pos[0] + dpos[0], self.pos[1] + dpos[1])

	def generatePath(self, pos):
		(x,y) = self.pos
		diff = (pos[0] - x, pos[1] - y)
		if diff == (-2, 1):
			return [ (x-1, y), (x-2, y), (x-2, y+1)]
		elif diff == (-2,-1):
			return [ (x-1, y), (x-2, y), (x-2, y-1)]
		elif diff == (2, -1):
			return [ (x+1, y), (x+2, y), (x+2, y-1)]
		elif diff == (2, 1):
			return [ (x+1, y), (x+2, y), (x+2, y+1)]
		elif diff == (1, 2):
			return [ (x, y+1), (x, y+2), (x+1, y+2)]
		elif diff == (-1, 2):
			return [ (x, y+1), (x, y+2), (x-1, y+2)]
		elif diff == (1, -2):
			return [ (x, y-1), (x, y-2), (x+1, y-2)]
		elif diff == (-1, -2):
			return [ (x, y-1), (x, y-2), (x-1, y-2)]

class Bishop(Piece):
	def __init__(self, pos, color):
		super().__init__(pos, color)
		self.type = "bishop"

	def possibeSquare(self, IMAX=8, JMAX=8):
		SIZE = max(IMAX, JMAX)
		for i in range(-int(0.5*SIZE), int(0.5*SIZE)+1):
			if i == 0:
				yield (self.pos[0] + i, self.pos[1] + i)
				yield (self.pos[0] + i, self.pos[1] - i)

	def generatePath(self, pos):
		path = []
		diff = pos[0] - self.pos[0]
		direction = 1 if diff > 0 else -1
		for i in range(diff + direction):
			if i > 0:
				path.append( (self.pos[0] + i, self.pos[1] + i))
		return path

class Rook(Piece):
	def __init__(self, pos, color):
		super().__init__(pos, color)
		self.type = "rook"

	def possibeSquare(self, IMAX=8, JMAX=8):
		SIZE = max(IMAX, JMAX)
		for i in range(-int(0.5*SIZE), int(0.5*SIZE)+1):
			if i == 0:
				yield (self.pos[0] + i, self.pos[1]    )
				yield (self.pos[0]    , self.pos[1] + i)

class Queen(Piece):
	def __init__(self, pos, color):
		super().__init__(pos, color)
		self.type = "queen"

	def possibeSquare(self, IMAX=8, JMAX=8):
		SIZE = max(IMAX, JMAX)
		for i in range(-int(0.5*SIZE), int(0.5*SIZE)+1):
			if i == 0:
				yield (self.pos[0] + i, self.pos[1]    )
				yield (self.pos[0]    , self.pos[1] + i)
				yield (self.pos[0] + i, self.pos[1] + i)
				yield (self.pos[0] + i, self.pos[1] - i)