import os
import pygame

imagelist = {}

def loadImage( filename, **options ):
	global imagelist
	# first test to see if we've already loaded the image
	if imagelist.has_key(filename) is False:
		# Then we need to load the image
		imagelist[filename] = pygame.image.load(filename)
		if imagelist[filename].get_alpha() is None:
			imagelist[filename] = imagelist[filename].convert()
		else:
			imagelist[filename] = imagelist[filename].convert_alpha()

	# Return the image
	return imagelist[filename]