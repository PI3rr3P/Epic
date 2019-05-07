from piece import *

class RulesException(Exception):
	def __init__(self, expression, message):
		self.expression = expression
		self.message = message

class Rules:
	''' Game logic
		Check the rules
		Allow and affect the moves
		Return message to the interface/Viewer
	'''

	# TODO
	# make choice on board / map representation
	#		board can allow make AI easier or AI should has several Rules ?
	#		board(s) can be thrown to viewer to plot the game
	# clean function isAllowedSquare
	# finish play_piece
	# satleman rules ?
	# you had to do something with isAble / isFreePath / isAllowed
	# ! Imax, Jmax a donner pour que les pieces fournissent des chemins ?

	def __init__(self):
		self.isEndGame = False
		self.players = [] # contain the pieces 
		self.board = [] # must be create somewhere [x][y](type, color)
		self.history = [] # list des coups joues depuis le debut AAAAAAAAAAAAA
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
		''' Heart of the game, try do that fucking move '''
		# if king move check final position must not be exposed

		msg = None
		(x,y) = pos
		if self.isChecked():  # must change that once piece move
			msg = []
		else :
			if self.current_piece.isAble(pos): # if arrival position is possible
				if self.board[x][y][0] != "rock": # if no rock at arrival
					if self.isFreePath(self.current_piece, pos): # no other piece/stuff on the road
						otherPiece = self.get_piece_at(pos)
						if otherPiece is None: # simple move
							msg = self.move(pos)
						elif piece.color != otherPiece.color: # attack
							msg = self.attack(other, pos)
		if msg is None: # move not valid
			msg = repr(self.current_piece)
			msg["action"] = "impossible"
		return msg

	def isAllowedSquare(self, piece, pos):
		''' Can a given piece be move at this position on board ? 
			possible if intrinsic able
			and if path is clear
			and if arrival is not occupy by same color or obstacle ?
		'''
		allow = True
		other = self.get_piece_at(pos)
		if other is not None:
			if other.color == piece.color:
				allow = False
		if not piece.isAble(pos):
			allow = False
		elif not piece.isFreePath( piece, pos ):
			allow = False
		return allow

	def isFreePath(self, piece, pos):
		''' given the way of moving a piece '''
		free = True
		if isinstance(piece, Knight) == False:
			path = piece.generatePath(pos)
			for pos in path[:-1]: # arrival position is questioned latter
				if self.board[pos[0]][pos[1]][0] is not None: # check if there is a piece on the path
					free = False
					break
				elif self.board[pos[0]][pos[1]][0] is not None: # check if there is a something on the path
					free = False
					break
		return free

	def move(self, pos):
		msg = repr(self.current_piece)
		msg["action"] = "move"
		msg["path"] = [self.current_piece.pos] + self.current_piece.generatePath(pos)
		self.updateBoard(pos)
		self.current_piece.pos = pos
		return msg

	def attack(self, victim, pos):
		msg = repr(self.current_piece)
		msg["action"] = "attack"
		msg["path"] = [self.current_piece.pos] + self.current_piece.generatePath(pos)
		self.updateBoard(pos)
		self.get_owner(victim).losePiece(victim) # deserve a try/catch with special error, piece without owner
		self.current_piece.pos = pos
		return msg

	def updateBoard(self, pos):
		(x,y) = self.current_piece.pos
		(u,v) = pos
		self.board[x][y] = (None, None)
		self.board[u][v] = (self.current_piece.type, self.current_piece.color)

	def isChecked(self):
		''' Is the current player in check ? '''
		isChecked = False
		king_pos = self.current_player.get_piece_type("king")
		if len(king_pos) != 0:
			raise RuleException("The current player possess no king")
		elif len(king_pos) > 1:
			raise RuleException("The current player possess more than one King")
		else:
			king_pos = king_pos[0]
			break_all = False
			for plyr in self.players:
				if plyr != self.current_player:
					for piece in plyr.pieces: 
						if piece.isAble(king_pos): 
							if self.isFreePath(piece, king_pos): 
								isChecked = True;
								break_all = True
								break;
					if break_all:
						break
		return isChecked

    def isStalemate(self):
    	''' Two conditions for stalemente
			King cannot move while being in danger
			All pieces cannot move
    	'''
    	isStalemate = False
    	isKingBlock = False
    	if len(self.current_player.piece) != 1:
		king = self.current_player.get_piece_type("king")
		if len(king) != 1:
			raise RuleException("The current player possess no king")
		# check king is block
		king = king[0]
		possible_king_pos = king.possibleSquare()
		for pos in possible_king_pos:
			if self.isAllowedSquare(king, pos) == False:
				possible_king_pos.remove(pos)
		break_all = False
		for plyr in [p for p in self.players if p != self.current_player]:
			for piece in plyr.pieces: 
				for pos in possible_king_pos:
					if piece.isAble(pos):
						if self.isFreePath(piece, pos): 
							possible_king_pos.remove(pos)
				if len(possible_king_pos) == 0:
					isKingBlock = True
					break_all = True
					break
			if break_all:
				break
		# check all other pieces
		if isKingBlock:
			break_all = False
			for piece in self.current_player.piece:
				possible_move = piece.possibleSquare()
				for pos in possible_move:
					if self.isAllowedSquare(piece, pos) == True:
						break_all = True
						break
				if break_all:
					break
			else:
				isStalemate = True
		return isStalemate

	def isCheckMate(self):
		''' Is the current player checkmate 
			heavy cost function
			check all possibility
			if no possibility to avoid the threat return True
		'''
		isCheckMate = False
		king = self.current_player.get_piece_type("king")[0]
		king_pos = king_pos
		# First solution : move the king
		#	find possible square for king
		possible_king_pos = king.possibleSquare()
		for pos in possible_king_pos:
			if self.isAllowedSquare(king, pos) == False:
				possible_king_pos.remove(pos)
		#	find if enemy can reach it
		for plyr in [p for p in self.players if p != self.current_player]:
			for piece in plyr.pieces:
				if piece.type != "king":
					for pos in possible_king_pos:
						if piece.isAble(pos):
							if self.isFreePath(piece, pos):
								possible_king_pos.remove(pos)
								break
		if len(possible_king_pos) == 0: # the king cannot move
			# Second solution : move another pieces
			#	find all critical path (= check path)
			critical_path = []
			for plyr in [p for p in self.players if p != self.current_player]:
				for piece in plyr.pieces:
					if piece.isAble(king_pos):
						if self.isFreePath(piece, king_pos):
							critical_path.append( [piece.pos] + piece.generatePath(king_pos)[:-1] )
			#	is there several threats ?
			if len(critical_path) == 1:
				break_all = False
				for pos in critical_path[0]: # can the critical path be intercepted by current players pieces ?
					for piece in [ p for p in self.current_player.pieces if p.type != "king" ]:
						if piece.isAble(pos):
							if self.isFreePath(piece, pos):
								break_all = True
								break
					if break_all:
						break
				else:
					isCheckMate = True
			else:
			#	if there an intersection between these threats ?
			#	one path cannot has several intersect with two convergeants paths because there are linear
				intersec = critical_path[0]
				for i, path in enumerate(critical_path[1:]):
					intersec = set(intersection).intersection(critical_path[i])
				if len(intersection) != 1: 
				# remain multiples threat (zero intersection or multiple intersection)
				# can't be discard at once, so player loose
					isCheckMate = True
				else:
				#	Can I set a piece on this single intersection ?
					intersec = intersec[0]
					break_all = False
					for piece in [ p for p in self.current_player.pieces if p.type != "king" ]:
						if piece.isAble(intersec):
							if self.isFreePath(piece, intersec):
								break_all = True
								break
						if break_all:
							break
					else:
						isCheckMate = True
		return isCheckMate


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

	def make_board(self):
		''' return a representation of the board '''
		board = self.map.make_board()
		for plyr in self.players:
			for piece in plyr.pieces:
				(x,y) = piece.pos
				if board[x][y] == ('Impossible', None):
					raise RulesException('Cannot set piece on this square {}'.format(piece.pos))
				else:
					board[][piece.pos[1]] = (piece.type, piece.color)
		return board

	def next_player(self):
		''' turn to next player in the list '''
		indexPlyr = (self.players.index( self.current_player ) + 1)
		self.current_player =  self.players[ indexPlyr % len(self.players) ]
		while self.current_player.alive != True: #SHOULD check for infinite loop
			indexPlyr += 1
			self.current_player =  self.players[ indexPlyr % len(self.players) ]
		self.selected_piece = None