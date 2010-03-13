from exceptions import Exception

class vector2DError(Exception):
	def __init__(self,args=None):
		self.args = args
	
import math
from math import pi

class vector2D(object):
	"""
		A simple 2D vector implementation
	"""
	
	# Arguements for an initialized vector given as x- and y- components. If you want to set angle and magnitude, initialize as a default vector and set them manually.
	def __init__( self, xvector = 0.0, yvector = 0.0 ):
		self.__x, self.__y = xvector, yvector
		self.__magnitude, self.__angle = 0.0,0.0
		self.__ConvertFromComponent2D()
		
	def __len__(self):
		return 2
		
	def __getitem__(self, key):
		if key == 0:
			return self.x
		elif key == 1:
			return self.y
		else:
			raise IndexError("Invalid subscript " + str(key) + "to vector2d")
	
	def __repr__(self):
		return 'vector2D(%s,%s)' % (self.x, self.y)
		
	# ConvertAngle2D and ConvertComponent2D are helper functions used internally to keep the x- and y-components and the angle and magnitude in sync.
	
	def __ConvertFromAngle2D(self):
		self.__x = float( self.__magnitude * math.cos( self.__angle ) )
		self.__y = float( self.__magnitude * math.sin( self.__angle ) )
		
	def __ConvertFromComponent2D(self):
		self.__magnitude = float( math.sqrt ( self.__x ** 2 + self.__y ** 2 ) )
		# This is the tricky bit. We have to adjust for the limited range of the inverse trig function.
		if self.__magnitude != 0:
			# If we're in quadrant I or IV we're okay
			if self.__x >= 0:
				rads = float( math.asin( self.__y / self.__magnitude ) )
				self.__angle = rads % ( 2 * pi )
			# Quadrant II and III
			else:
				rads = pi - float ( math.asin ( self.__y / self.__magnitude ) )
				self.__angle = rads
		else:
			self.__angle = 0
		
	# Properties
	# This is to allowe controlled outside access to the the vector components and magnitude/angle, and still keep them synched up.

	# Property for x-component
	def getx(self):
		return self.__x
	
	def setx(self, value ):
		self.__x = value
		self.__ConvertFromComponent2D()

	x = property(getx, setx, None, "The x component of the vector")

	# Property for y-component	
	def gety(self):
		return self.__y
	
	def sety(self, value ):
		self.__y = value
		self.__ConvertFromComponent2D()

	y = property(gety, sety, None, "The y component of the vector")
	
	# Property for angle
	def getangle(self):
		return self.__angle
	
	def setangle( self, value ):
		# Constrain it to a 2 pi radius
		self.__angle = value % ( 2 * pi )
		self.__ConvertFromAngle2D()

	angle = property(getangle, setangle, None, "The angle of the vector")
	
	def getdegree(self):
		# Convert radian to degree
		return self.__angle * ( 180 / pi )
		
	def setdegree(self, value):
		self.__angle = float ( ( value % 360 ) * ( pi / 180 ) )
		self.__ConvertFromAngle2D()
		
	degree = property(getdegree, setdegree, None, "The angle of the vector in degrees")
	
	# Property for magnitude
	def getmagnitude(self):
		return self.__magnitude
	
	def setmagnitude( self, value ):
		self.__magnitude = value
		self.__ConvertFromAngle2D()

	magnitude = property(getmagnitude, setmagnitude, None, "The magnitude of the vector")
		
	
	# Vector addition
	def __add__(self, other):
		if hasattr(other, "__getitem__"):
			return vector2D( self.x + other[0], self.y + other[1])
		else:
			raise vector2Derror("I don't know how to talk to that!")
	def __radd__(self, other):
		if hasattr(other, "__getitem__"):
			return vector2D( self.x + other[0], self.y + other[1])
		else:
			raise vector2Derror("I don't know how to talk to that!")
	
	def __iadd__(self, other):
		if hasattr(other, "__getitem__"):
			self.__x += other[0]
			self.__y += other[1]
			self.__ConvertFromComponent2D()
		else:
			raise vector2Derror("I don't know how to talk to that!")
		return self
	
	# Negation.
	def __neg__(self):
		return vector2D(-self.x, -self.y)
	
	def __sub__(self, other):
		if hasattr(other,"__getitem__"):
			return vector2D( self.x - other[0], self.y - other[1])
		else:
			raise vector2Derror("I can't talk to that!")
	
	def __rsub__(self, other):
		if hasattr(other,"__getitem__"):
			return vector2D( other[0] - self.x, other[1] - self.y )
		else:
			raise vector2Derror("I can't talk to that!")
	
	def __isub__(self, other):
		if hasattr(other, "__getitem__"):
			self.x -= other[0]
			self.y -= other[1]
			self.__ConvertFromComponent2D()
		else:
			raise vector2Derror("I don't know how to talk to that!")
		return self
			
	
# Vector testing to make sure we got it all right.
if __name__ == "__main__":
	
	def vecprint( vector ):
		print "(X/Y:%f/%f) (A/D/M:%f/%f/%f)" % ( vector.x, vector.y, vector.angle, vector.degree, vector.magnitude )
	
	# First we'll test creation of a bunch of different vectors
	vectorpairs = [ (0,0), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1),(0,-1),(1,-1) ]
	vectors = []
	for x in range(0,9):
		vectors.append( vector2D() )
		vectors[x].x, vectors[x].y = vectorpairs[x]

	print "Vectors created successfully."
	
	# Let's make sure everything actually works properly
	
	for v in vectors:
		vecprint ( v )
		
	print "I'm not sure the angles are working properly... this is further testing."
	
	print ">> Starting with a fresh vector."
	v1 = vector2D( 5, 0 )
	print ">> v1: %r" % v1
	print ">> Adding 45 degree increments"
	for x in range( 0, 2 * pi + pi / 8, pi / 2 ):
		v1.angle = x
		vecprint(v1)
		
	v1 = vector2D( 1, 0 )
	v2 = vector2D ( 2, 0 )
	v3 = vector2D ( 0, 1 )
	
	print ">> Vector math testing!"
	for v in [ v1, v2, v3 ]:
		vecprint(v)
		
	print ">> v1 + v2 = "
	vecprint(v1+v2)
	print ">> v1 + (0,4)"
	vecprint(v1+(0,4))
	print ">> (0,4) + v1"
	vecprint((0,4) + v1)
	print ">> v1 += (0,1)"
	v1+=(0,1)
	vecprint(v1)
	
	print ">> v1 -= (0,1)"
	v1 -= (0,1)
	vecprint(v1)
	print ">> v2 - v1 "
	vecprint(v2-v1)
	print ">> v2 - (1,0)"
	vecprint(v2-(1,0))
	print ">> (3,0) - v2"
	vecprint((3,0) - v2)