class Rules:
	''' Game logic
		Check the rules
		Allow and affect the moves
	'''

	def __init__(self):
		self.isEndGame = False
		self.players = [] # contain the pieces 
		self.board = None # must be create somewhere
		self.current_player = None # must be selected somehow
		self.current_piece = None # handle

	def select_piece(self, pos):
		selected_piece = self.get_piece_at(pos)
		if selected_piece in self.current_player.piece:
			self.current_piece	== selected_piece
			msg = repr(self.current_piece)
			msg["action"] = "selected"
			return msg
		else: 
			self.current_piece = None
			return None

	def play_piece(self, pos):
		msg = ''
		if not self.isChecked():
			if pos in self.current_piece.possibleSquare():
				if self.board.at(pos) == "empty":
					# check path (knight don't care)
					# check destination
					otherPiece = self.get_piece_at(pos)
					if otherPiece is None:
					elif piece.color != otherPiece.color:
						# check if the path is possible
							# simple move
							# attack
					else:
						# not possible
				# affect the move
		return msg

	def findPath(self, pos):
		''' given the way of moving a piece '''
		path = self.current_piece.generatePath(pos)
		for square in path[:-1]:
			if self.get_piece_at(pos) is not None:
				return None
		else
			return path

	def move(self, other):
		pass

	def attack(self):
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

	def isAllowed(self): # useless
		''' move is allowed if square exist / square not block / other piece is not same color ''' 
		allowed = False
		if self.board.at(pos) == "empty":
			otherPiece = self.get_piece_at(pos)
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

	def attack(self, attacker, victim ):
		self.animation_stack.append( ('attack', attacker, victim) )
		self.select_piece.pos = victim.pos
		self.get_owner.remove(victim) # deserve a try/catch with special error, piece without owner

	def isChecked(self):
		''' Is the current player in check '''
		raise NotImplementedException()

	def get_piece_at(self, pos):
		piece = None
		for plyr in self.players:
			piece = plyr.get_piece_at(pos)
			if piece is not None:
				break
		return piece
	
	def get_owner(self, piece):
		owner = None
		for plyr in self.players:
			if piece in plyr.pieces:
				owner = plyr
				break
		return owner

	def next_player(self):
		''' turn to next player in the list '''
		self.current_player =  self.players[ (self.players.index( self.current_player ) + 1) % len(self.players) ]
		self.selected_piece = None