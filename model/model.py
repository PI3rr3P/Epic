class Model:
	def __init__(self): # give players and map ?
		self.rules = Rules()
		self.piece_selected = False
		self.animation_stack = []
		self.pieces_stack = []

	def select_piece(self, pos):
		msg = self.rules.select_piece(pos)
		if msg is not None:
			self.piece_selected = True
			self.animation_stack.append( msg )

	def play_piece(self, pos):
		if self.piece_selected == True:
			msg = self.rules.play_piece(pos)
			if msg is not None:
				# move accepted
				self.animation_stack.append( msg )
				self.piece_selected = False

	def unstack_animation():
		pass

# structural problems:
# 	isInChess => regarder si la position du roi (juste donner piece.pos) est attaquee
#	