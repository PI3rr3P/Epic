class Player:

	def __init__(self, color):
		self.pieces = []
		self.color = color
		self.status = "alive"

	def losePiece(self, piece):
		self.pieces.remove(piece)

	def gainPiece(self, piece):
		self.pieces.append(piece)

	def get_piece_at(self, pos):
		piece = None
		for elt in self.pieces:
			if elt.pos == pos:
				piece = elt
				break
		return piece