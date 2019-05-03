from piece import *

class RulesException(Exception):
	def __init__(self, expression, message):
		self.expression = expression
		self.message = message

class Rules:
	''' Game logic
		Check the rules
		Allow and affect the moves
		Return message to the interface
	'''

	def __init__(self):
		self.isEndGame = False
		self.players = [] # contain the pieces 
		self.board = [] # must be create somewhere [x][y](type, color)
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
		msg = None
		(x,y) = pos
		if self.isChecked():  # must move king if it is in danger
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
		else:
			for pos in king_pos: # case where the current player has sevaral kings
				for plyr in self.players:
					if plyr != self.current_player:
						for piece in plyr.pieces: 
							if piece.isAble(king_pos): 
								if self.isFreePath(piece, king_pos): 
									isChecked = True;
									break;
		return isChecked

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
		indexPlyr = (self.players.index( self.current_player ) + 1)
		self.current_player =  self.players[ indexPlyr % len(self.players) ]
		while self.current_player.alive != True: #SHOULD check for infinite loop
			indexPlyr += 1
			self.current_player =  self.players[ indexPlyr % len(self.players) ]
		self.selected_piece = None