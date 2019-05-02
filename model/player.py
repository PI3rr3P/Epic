class Player:

	def __init__(self, color):
		self.pieces = []
		self.color = color
		self.status = "alive"

	def losePiece(self, piece):
		self.pieces.remove(piece)
		if len(self.pieces) == 0:
			self.status = "die"

	def gainPiece(self, piece):
		self.pieces.append(piece)

	def get_piece_at(self, pos):
		piece = None
		for elt in self.pieces:
			if elt.pos == pos:
				piece = elt
				break
		return piece

	def get_piece_type(self, kind):
		all_kind_piece = []
		for piece in self.pieces:
			if piece.type == kind:
				all_kind_piece.append(piece)
		return all_kind_piece