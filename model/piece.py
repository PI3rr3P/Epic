class MouvementError(Exception):
	''' position error '''
	def __init__(self, expression, message):
		self.expression = expression
		self.message = message

class Piece:
	def __init__(self, pos, color):
		self.pos = pos
		self.oldPos = []
		self.type = "abstract"
		self.color = "void"
		self.neverMove = True

	def isAble(self, pos):
		''' basic allowed move '''
		return False

	def possibleSquare(self, IMAX=None, JMAX=None):
		''' give possible position give a type of piece '''
		yield None

	def generatePath(self, pos):
		''' give the way the piece go, return a serie of position '''
		return []

	def generateGraphicPath(self, pos):
		return self.generatePath(pos)

	def __repr__(self):
		return {'type': self.type, 'color': self.color, 'pos':self.pos}

class King(Piece):
	def __init__(self, pos, color):
		super().__init__(pos, color)
		self.type = "king"

	def isAble(self, pos):
		allowed = False
		(x,y) = self.pos
		(u,v) = pos
		if abs(x - u) == 1 and abs(y - v) == 1:
			allowed = True
		return False

	def possibeSquare(self, IMAX=None, JMAX=None):
		for i in range(-1,1):
			for j in range(-1,1):
				if i == 0 or j == 0:
					yield (self.pos[0] + i, self.pos[1] + j)

	def generatePath(self, pos):
		if abs(self.pos[0] - pos[0]) == 1 and abs(self.pos[1] - pos[1]) == 1:
			return [pos]
		else:
			raise MouvementError("King cannot do such move : {} -> {}".format(self.pos, pos))

class Pawn(Piece):
	def __init__(self, pos, color):
		super().__init__(pos, color)
		self.type = "pawn"

	def isAble(self, pos):
		allowed = False
		(x,y) = self.pos
		(u,v) = pos
		if (y - v) == 1 and abs(x - u) <= 1:
			allowed = True
		return allowed

	def possibeSquare(self):
		possible = [ (0, 1), (1,1), (-1, -1)]
		for dpos in possible:
			yield (self.pos[0] + dpos[0], self.pos[1] + dpos[1])

	def generatePath(self, pos):
		if abs(pos[0] - self.pos[0]) == 1 and ((pos[1] - self.pos[1]) == 1):
			return [pos]
		else:
			raise MouvementError("Pawn cannot do such move : {} -> {}".format(self.pos, pos))

class Knight(Piece):
	def __init__(self, pos, color):
		super().__init__(pos, color)
		self.type = "knight"

	def isAble(self, pos):
		allowed = False
		(x,y) = self.pos
		(u,v) = pos
		if ( abs(y - v) == 2 and abs(x - u) == 1) or (abs(x - u) == 2 and abs(y -v) == 1):
			allowed = True
		return allowed

	def possibeSquare(self):
		possible = [ (-2, 1), (-2,-1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
		for dpos in possible:
			yield (self.pos[0] + dpos[0], self.pos[1] + dpos[1])

	def generatePath(self, pos):
		if ( pos[0] - self.pos[0], pos[1] - self.pos[1]) in [ (-2, 1), (-2,-1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]:
			return [pos]
		else:
			raise MouvementError("Knight cannot do such move : {} -> {}".format(self.pos, pos))

	def generateGraphicPath(self, pos):
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
		else
			raise MouvementError("Knight cannot do such move : {} -> {}".format(self.pos, pos))

class Bishop(Piece):
	def __init__(self, pos, color):
		super().__init__(pos, color)
		self.type = "bishop"

	def isAble(self, pos):
		allowed = False
		(x,y) = self.pos
		(u,v) = pos
		if abs(x - u) == abs(y - v):
			allowed = True
		return allowed

	def possibeSquare(self, IMAX=8, JMAX=8):
		SIZE = max(IMAX, JMAX)
		for i in range(-int(0.5*SIZE), int(0.5*SIZE)+1):
			if i == 0:
				yield (self.pos[0] + i, self.pos[1] + i)
				yield (self.pos[0] + i, self.pos[1] - i)

	def generatePath(self, pos):
		path = []
		diff_x = pos[0] - self.pos[0]
		direction_x = 1 if diff_x > 0 else -1
		diff_y = pos[1] - self.pos[1]
		direction_y = 1 if diff_y > 0 else -1
		if abs(diff_x) != abs(diff_y):
			raise MouvementError("Bishop cannot do such move : {} -> {}".format(self.pos, pos))
		for (x, y) in zip(range(diff_x + direction_x), range(diff_y + direction_y)):
			if x != 0 and y != 0:
				path.append( (self.pos[0] + x, self.pos[1] + y))
		return path

class Rook(Piece):
	def __init__(self, pos, color):
		super().__init__(pos, color)
		self.type = "rook"

	def isAble(self, pos):
		allowed = False
		(x,y) = self.pos
		(u,v) = pos
		if (abs(x - u) == 0 and abs(y - v) > 0) or (abs(y - v) == 0 and abs(x - u) > 0):
			allowed = True
		return allowed

	def possibeSquare(self, IMAX=8, JMAX=8):
		SIZE = max(IMAX, JMAX)
		for i in range(-int(0.5*SIZE), int(0.5*SIZE)+1):
			if i != 0:
				yield (self.pos[0] + i, self.pos[1]    )
				yield (self.pos[0]    , self.pos[1] + i)

	def generatePath(self, pos):
		path = []
		tmp_pos = self.pos
		diff_x = pos[0] - self.pos[0]
		direction_x = 1 if pos[0] > self.pos[0] else -1
		diff_y = pos[1] - self.pos[1]
		direction_y = 1 if pos[1] > self.pos[1] else -1
		if diff_x != 0 and diff_y == 0:
			for x in range(diff_x + direction_x):
				if x != 0
					tmp_pos = (tmp_pos[0] + x, tmp_pos[1])
					path.append(tmp_pos)
		elif diff_y != 0 and diff_x == 0:
			for y in range(diff_y + direction_y):
				if y != 0:
					tmp_pos = (tmp_pos[0], tmp_pos[1] + y)
					path.append(tmp_pos)
		else:
			raise MouvementError("Rook cannot do such move : {} -> {}".format(self.pos, pos))
		return path

class Queen(Piece):
	def __init__(self, pos, color):
		super().__init__(pos, color)
		self.type = "queen"

	def isAble(self, pos):
		allowed = False
		(x,y) = self.pos
		(u,v) = pos
		if abs(x - u) == abs(y - v):
			allowed = True
		elif (abs(x - u) == 0 and abs(y - v) > 0) or (abs(y - v) == 0 and abs(x - u) > 0):
			allowed = True
		return allowed

	def possibeSquare(self, IMAX=8, JMAX=8):
		SIZE = max(IMAX, JMAX)
		for i in range(-int(0.5*SIZE), int(0.5*SIZE)+1):
			if i != 0:
				yield (self.pos[0] + i, self.pos[1]    )
				yield (self.pos[0]    , self.pos[1] + i)
				yield (self.pos[0] + i, self.pos[1] + i)
				yield (self.pos[0] + i, self.pos[1] - i)

	def generatePath(self, pos):
		path = []
		tmp_pos = self.pos
		diff_x = pos[0] - self.pos[0]
		direction_x = 1 if pos[0] > self.pos[0] else -1
		diff_y = pos[1] - self.pos[1]
		direction_y = 1 if pos[1] > self.pos[1] else -1
		if diff_x != 0 and diff_y == 0:
			for x in range(diff_x + direction_x):
				if x != 0
					tmp_pos = (tmp_pos[0] + x, tmp_pos[1])
					path.append(tmp_pos)
		elif diff_y != 0 and diff_x == 0:
			for y in range(diff_y + direction_y):
				if y != 0:
					tmp_pos = (tmp_pos[0], tmp_pos[1] + y)
					path.append(tmp_pos)
		elif abs(diff_x) == abs(diff_y):
			for (x, y) in zip(range(diff_x + direction_x), range(diff_y + direction_y)):
				if x != 0 and y != 0:
					tmp_pos = (tmp_pos[0] + x, tmp_pos[1] + y)
					path.append(tmp_pos)
		else:
			raise MouvementError("Queen cannot make such move : {} -> {}".format(self.pos, pos))
		return path