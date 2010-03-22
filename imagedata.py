import pygame
from vector2D import vector2D

class sprite(object):
	def __init__(self, filename):

		#If we're not going to use this function ANYWHERE ELSE
		#why expose it?  Make it a local function.
		def loadImage(filename):
			image = pygame.image.load(filename)
			if image.get_alpha() is None:
				image = image.convert()
			else:
				image = image.convert_alpha()
			return image

		self.image = loadImage(filename)
		self.angle = vector2D(1,0)
		self.position = vector2D(0,0)
		
	def draw( self, surface ):
		# And now we rotate the image first
		imagecopy = self.image
		imagecopy = pygame.transform.rotate(imagecopy, self.angle.degree)
		# We're drawing by image center, so...
		surface.blit( imagecopy, self.position - ( imagecopy.get_width() / 2, imagecopy.get_height() / 2 ) )
