import resources
from pygame import transform
from vector2D import vector2D

class sprite(object):
	def __init__(self, filename):
		self.image = resources.imageManager.loadImage(filename)
		self.angle = vector2D(1,0)
		self.position = vector2D(0,0)
		
	def draw( self, surface ):
		# And now we rotate the image first
		imagecopy = self.image
		imagecopy = transform.rotate(imagecopy, self.angle.degree)
		# We're drawing by image center, so...
		surface.blit( imagecopy, self.position - ( imagecopy.get_width() / 2, imagecopy.get_height() / 2 ) )