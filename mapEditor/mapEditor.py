import pygame
from pygame.locals import *

class MapEditor:
	_squareSize = 25

	def __init__(self, mapName, Imax, Jmax):
		self.mapName = mapName
		self.Imax = Imax
		self.Jmax = Jmax
		self.map = []
		self.picture = []
		self.img = {}
		self.initMap()
		self.screen = pygame.display.set_mode((Imax * _squareSize, Jmax * _squareSize))
		self.screen.fill(self.WHITE)

	def load_picture(self):
		''' must load all image '''
		self.img[('Pawn', 'red')] = pygame.image.load("").convert_alpha()

	def initMap(self):
		''' init a void map '''
		for j in range(self.Jmax):
			raw = []
			for i in range(self.Imax):
				raw.append( (None, None) )
			self.map.append(raw)

	def 