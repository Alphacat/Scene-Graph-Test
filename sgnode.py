# Scene graph implementation

class sgnode(object):
	ids = 0
	nodelist = []
	
	# Don't override this unless you need to change the default behaviour,
	#  but make sure all this is set up correctly. You should probably use
	#  doStartup() instead.
	def __init__(self, parent, **args):
		self.childlist = []
		
		self.parent = parent
		if parent is not None:
			parent.addNode(self)
			
		self.id = sgnode.ids
		sgnode.ids += 1
		sgnode.nodelist.append(self)
		
		# Here we'll do specific startup stuff.
		doStartup(**args)
		
		# And that should be it.
	
		
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
		
class spritenode(sgnode):
	def doStartup( args ):
		self.sprite = args["sprite"]
		
	