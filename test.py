import pygame
from sgnode import sgnode
from vector2D import vector2D
import imagedata

class baseGame(object):
	def __init__(self, resolution=(640,480)):
		pygame.init()
		self.screen = pygame.display.set_mode(resolution)
		self.clock = pygame.time.Clock()

		self.mysprite = imagedata.sprite("test2.png")
		self.mysat = imagedata.sprite("test3.png")
		self.mysatvec = vector2D(50,0)

	def Run(self):
		loop_cont = True
		while loop_cont:
			time_passed = self.clock.tick(40)
			pygame.display.set_caption("time_passed: %i fps: %f " %
					(time_passed, self.clock.get_fps()))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return

			self.screen.fill((0, 0, 96))
			
			scalar = time_passed / 1000.0
			self.mysprite.angle.degree += (180 * scalar)
			self.mysprite.position += (5 * scalar, 5 * scalar)

			self.mysat.position = self.mysprite.position + self.mysatvec
			self.mysatvec.degree -= 1.5
			self.mysat.angle.degree -= 2.1

			self.mysprite.draw(self.screen)
			self.mysat.draw(self.screen)

			pygame.display.flip()

myGame = baseGame()
myGame.Run()
