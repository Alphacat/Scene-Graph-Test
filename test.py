import pygame
import resources
from sgnode import sgnode
from sprite import sprite
from vector2D import vector2D



# Initialize game parameters
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = 0, 0, 96
screen = None
clock = None

def game_init():
	global clock, screen
	pygame.init()
	screen = pygame.display.set_mode( SCREEN_SIZE )
	clock = pygame.time.Clock()
	
def game_main():
	global screen, clock
	
	# This is a test
	test1 = resources.imageManager.loadImage("test.png")
	test2 = resources.imageManager.loadImage("test.png")
	testcopy = resources.imageManager.loadImage("test.png" )
	
	
	test2a = pygame.image.load("test.png")
	test2b = pygame.image.load("test.png")
	
	mysprite = sprite( "test2.png" )
	mysat1 = sprite("test3.png")
	mysat1vec = vector2D(50,0)
	
	loop_cont = True
	while loop_cont:
		time_passed = clock.tick(40)
		pygame.display.set_caption( "time_passed: %i fps: %f " %  ( time_passed, clock.get_fps() ) )
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill( BG_COLOR )
		
		#screen.blit( test1, (0,0) )
		#screen.blit( test2, (160,0) )
		#screen.blit( testcopy, ( 0, 320 ) )
		scalar = time_passed / 1000.0
		mysprite.angle.degree += ( 180 * scalar )
		mysprite.position += (5 * scalar,5 * scalar)
		
		mysat1.position = mysprite.position + mysat1vec
		mysat1vec.degree -= 1.5
		mysat1.angle.degree -= 2.1
		
		mysprite.draw(screen)
		mysat1.draw(screen)
		
		pygame.display.flip()
		
def game_quit():
	pass
	

# Main()
game_init()
game_main()
game_quit()