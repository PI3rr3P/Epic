class Rules:

	def __init__(self):
		pass

	def isAble(self, piece, pos):
		allowed = False
		(x,y) = piece.pos
		(u,v) = pos
		if piece.type == "king":
			if abs(x - u) == 1 and abs(y - v) == 1:
				allowed = True
		elif piece.type == "queen":
			if abs(x - u) == abs(y - v): # diagonal
				allowed = True
			elif (abs(x - u) == 0 and abs(y - v) > 0) or (abs(y - v) == 0 and abs(x - u) > 0):
				allowed = True
		elif piece.type == "rook":
			if (abs(x - u) == 0 and abs(y - v) > 0) or (abs(y - v) == 0 and abs(x - u) > 0):
				allowed = True
		elif piece.type == "knight":

		elif piece.type == "bishop":
			if abs(x - u) == abs(y - v): # diagonal
				allowed = True
		elif piece.type == "pawn":
			# NOT FINISHED
			if ( (y - v)  == 1 and (x == u) ) or ( (y - v) == -1):
				allowed = True
		return allowed

	def isAllowed(self, piece, otherPiece, boardSquare):
		allowed = False
		if piece.color != otherPiece.color and boardSquare == "empty":
			
