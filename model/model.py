class Model:
	def __init__(self): # give player and map ?
		self.rules = Rules()
		self.players = [] # contain the pieces 
		self.board = None # must be create somewhere
		self.animation_pile = []
		self.current_player = None # must be selected somehow
		self.current_piece = None # handle

	def select_piece(self, pos):
		piece = self.current_player.get_piece_at(pos)
		if piece != None:
			self.current_piece = piece
			self.animation_pile.append( ('select', elt) ) # viewer draw selected square and draw possible move ?
			self.animation_pile.append( ('possibility', [POSITION_LIST], [ATTACKED_PIECE] ) ) # print possible move ? 
			break

	def play_piece(self, pos):
		if self.rules.isAble(self.current_piece, pos):
			otherPiece = self.get_piece_at(pos)
			squareStatus = self.board.get_square_status(pos)
			if self.rules.isAllow(self.current_piece, otherPiece, squareStatus):
				action = self.rules.actionType(self.current_piece, otherPiece, squareStatus)
				if action == "attack":
					self.move()
				elif action == "move":
					self.attack(otherPiece)
				self.current_piece = None
				self.current_player = self.next_player()

	def move(self, pos):
		self.animation_pile.append( ('move', piece) )
		self.select_piece = pos

	def attack(self, attacker, victim ):
		self.animation_pile.append( ('attack', attacker, victim) )
		self.select_piece.pos = victim.pos
		self.get_owner.remove(victim) # deserve a try/catch with special error, piece without owner

	def get_piece_at(self, pos):
		piece = None
		for plyr in self.players:
			if plyr.get_piece_at(pos) is not None:
				piece = plyr.get_piece_at(pos)
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
		return self.players[ (self.players.index( self.current_player ) + 1) % len(self.players) ]

	def unstack_animation():
		pass

# structural problems:
# 	isInChess => regarder si la position du roi (juste donner piece.pos) est attaquee
#	