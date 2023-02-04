import sys

try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("ERROR: loading launchpad.py failed")

limit  = lambda n, minVal, maxVal: max( min( maxVal, n ), minVal )
limit1 = lambda n: limit( n, 0.0, 1.0 )

class Display():
	def __init__( self ):
		# remember the Launchpad type to adjust the mapping of the buttons
		self.mode = None

		# create an instance
		lp = launchpad.Launchpad()

		# try the first Mk2
		if lp.Check( 0, "mk2" ):
			lp = launchpad.LaunchpadMk2()
			if lp.Open( 0, "mk2" ):
				print( " - Launchpad Mk2: OK" )
				self.mode = "mk2"
			else:
				print( " - Launchpad Mk2: ERROR")
				return
			
		# try the first Mini Mk3
		elif lp.Check( 1, "minimk3" ):
			lp = launchpad.LaunchpadMiniMk3()
			if lp.Open( 1, "minimk3" ):
				print( " - Launchpad Mini Mk3: OK" )
				self.mode = "mk3"
			else:
				print( " - Launchpad Mini Mk3: ERROR")
				return

		# try the first Pro
		elif lp.Check( 0, "pad pro" ):
			lp = launchpad.LaunchpadPro()
			if lp.Open( 0, "pad pro" ):
				print( " - Launchpad Pro: OK" )
				self.mode = "pro"
			else:
				print( " - Launchpad Pro: ERROR")
				return

		# try the first Pro Mk3
		elif lp.Check( 0, "mk3" ):
			lp = launchpad.LaunchpadProMk3()
			if lp.Open( 0 ):
				print( " - Launchpad Pro Mk3: OK" )
				self.mode = "promk3"
			else:
				print( " - Launchpad Pro Mk3: ERROR")
				return

		# try the first X
		# Notice that this is already built-in in the LPX class' methods Check() and Open,
		# but we're using the one from above!
		elif lp.Check( 1, "Launchpad X") or lp.Check( 1, "LPX" ):
			lp = launchpad.LaunchpadLPX()
			# Open() includes looking for "LPX" and "Launchpad X"
			if lp.Open( 1 ):
				print( " - Launchpad X: OK" )
				self.mode = "lpx"
			else:
				print( " - Launchpad X: ERROR")
				return

		# nope
		else:
			raise Exception("No compatible Launchpad found. Only for Mk2, Mk3, Pro")

		self.lp = lp

	def LiveMode( self ):
		if self.mode == "promk3":
			self.lp.LedSetMode( 0 )

	def Clear( self ):
		self.lp.Reset()

	def Close( self ):
		self.lp.Close()

	def ButtonGet( self ):
		if self.mode == "pro" or self.mode == "promk3":
			return self.lp.ButtonStateXY( mode = "pro" )
		elif self.mode == "mk3" or self.mode == "lpx":
			return self.lp.ButtonStateXY( mode = "classic" )
		elif self.mode == "mk2":
			return self.lp.ButtonStateXY()

		return []

	def setLED(self, x, y, r, g, b):
		self.lp.LedCtrlXY(x, y, r, g, b)