# Scene graph implementation
from vector import vector2D

class sgnode(object):
	ids = 0
	nodelist = []
	
	# Don't override this unless you need to change the default behaviour,
	#  but make sure all this is set up correctly. You should probably use
	#  doStartup() instead.
	def __init__(self, parent, xpos = 0, ypos = 0, angle = 0.0, xsize = 1.0, ysize = 1.0, **args):
		self.childlist = []
		
		self.parent = parent
		if parent is not None:
			parent.addNode(self)
			
		self.id = sgnode.ids
		sgnode.ids += 1
		sgnode.nodelist.append(self)
		
		# Setup base node properties
		self.__position = vector2D( xpos, ypos )
		self.__angle = vector2D()
		self.__angle.angle = angle
		self.__size = vector2D( xsize, ysize )
		
		# Here we'll do specific startup stuff.
		doStartup(**args)
		
		# And that should be it.
		
	# Properties
	# Position functions
	def getpos(self):
		return self.__position
		
	def setpos(self, value): # Set the x and y vectors wholesale
		self.__position = value
		
	position = property(getpos, setpos, None, "Sets the position vector")
	
	def getposx(self):
		return self.__position.x
		
	def setposx(self, value):
		self.__position.x = value
		
	posx = property(getposx, setposx, None, "Sets the x-coordinate of the position")

	def getposy(self):
		return self.__position.y
		
	def setposy(self, value):
		self.__position.y = value
		
	posy = property(getposy, setposy, None, "Sets the y-coordinate of the position")	
	
	# Angle
	def getangle(self):
		return self.__angle.angle
	
	def setangle(self, value):
		self.__angle.angle = value
		
	angle = property(setangle, getangle, None, "Gets the angle of the node")
	
	def getangledegree(self):
		return self.__angle.degree
	
	def setangledegree(self, value):
		self.__angle.degree - value
		
	angledegree = property(setangledegree, getangledegree, None, "Gets the degree of the node in degrees (not radians)")
	
	# Size
	def getsize(self): # Returns (xsize, ysize)
		return self.__size
	
	def setsize(self, value): # Set both xsize and ysize in one shot
		self.__size.x, self.__size.y = value, value
		
	size = property( getsize, setsize, None, "Property to get or set both size values at once")
	
	def getsizex(self):
		return self.__size.x
		
	def setsizex(self, value):
		self.__size.x = value
		
	sizex = property( getsizex, setsizex, None, "Property to get or modify the x scalar" )
	
	def getsizey(self):
		return self.__size.y
		
	def setsizey(self, value):
		self.__size.y = value
		
	sizey = property( getsizey, setsizey, None, "Property to get/modify the y scalar")
	
		
	# Specific setup for specialized node types
	def doStartup():
		pass
		
	# Generic render function
	def render( options ):
		# Set up the render task
		self.setupRender( options )
		
		# Call specific render function
		self.doRender( options )
		
		for node in childlist:
			node.render( options )
			
		# Reset options back to their previous state
		self.cleanupRender( options )
	
	def setuprender( options ):
		pass
			
	def doRender( options ):
		pass
		
	def cleanupRender( options ):
		pass
