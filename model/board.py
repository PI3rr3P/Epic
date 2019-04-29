class Board:

	def __init__(self, mapFile):
		self.map = []
		self.readMap(mapFile)

	def readMap(self, mapFile):
		""" read form a txt file """
		self.map = []
		with open(mapFile, 'r') as mapTxt:
			for lines in mapTxt:
				self.map.append( [  word for word in lines.split() if word != '\n'] )
		# must check is square

	def color(self, pos):
		""" white = True, black = False """
		(x, y) = pos
		if abs(y - x + 1) % 2 == 0:
			return True
		else:
			return False

	def occupied(self, pos):
		""" True if occupied """
		(x, y) = pos
		if self.map[x][y] == "b":
			return True
		else:
			return False