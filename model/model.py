class Model:
	def __init__(self):
		self.rules = Rules()
		self.pieces = []
		self.players = []
		self.current_player = None
		self.current_piece = None

	def select(self, pos):
		for elt in self.pieces:
			if elt.pos == pos and self.current_player.color == elt.color:
				self.current_piece = elt
				# register animation selection
				break

	def move(self, pos):
		if self.rules.isAllow(self.current_piece, pos):
			
