class Rules:

	def __init__(self):
		pass

	def isAble(self, piece, pos):
		''' basic allowed move '''
		allowed = False
		(x,y) = piece.pos
		(u,v) = pos
		if piece.type == "king":
			if abs(x - u) == 1 and abs(y - v) == 1:
				allowed = True
		elif piece.type == "queen":
			if abs(x - u) == abs(y - v):
				allowed = True
			elif (abs(x - u) == 0 and abs(y - v) > 0) or (abs(y - v) == 0 and abs(x - u) > 0):
				allowed = True
		elif piece.type == "rook":
			if (abs(x - u) == 0 and abs(y - v) > 0) or (abs(y - v) == 0 and abs(x - u) > 0):
				allowed = True
		elif piece.type == "knight":
			if ( abs(y - v) == 2 and abs(x - u) == 1) or (abs(x - u) == 2 and abs(y -v) == 1):
				allowed = True
		elif piece.type == "bishop":
			if abs(x - u) == abs(y - v):
				allowed = True
		elif piece.type == "pawn":
			if (y - v) == 1 and abs(x - u) <= 1:
				allowed = True
		return allowed

	def isAllowed(self, piece, otherPiece, boardSquare):
		''' move is allowed if square exist / square not block / other piece is not same color ''' 
		allowed = False
		if boardSquare == "empty":
			if otherPiece == None:
				allowed = True
			elif piece.color != otherPiece.color:
				allowed = True
		return allowed 

	def actionType(self, piece, otherPiece, boardSquare):
		''' is it a move or an attack '''
		if piece.color != otherPiece.color:
			return "attack"
		else:
			return "move"