# Imports -----------------------------------------------
import xbmc, xbmcaddon
import httplib


# Settings -----------------------------------------------
settings  = xbmcaddon.Addon(id="service.kodi.anna")
 

# Classes ------------------------------------------------
class Anna(xbmc.Player):
	def __init__(self, *args):
		pass

	def onPlayBackStarted(self):
		self.request(False)

	def onPlayBackPaused(self):
		self.request(True)

	def onPlayBackResumed(self):
		self.request(False)

	def onPlayBackEnded(self):
		self.request(True)

	def onPlayBackStopped(self):
		self.request(True)

	def request(self,switchOn):
		hostname = settings.getSetting("hostname")
		port = settings.getSetting("port")
		deviceid = settings.getSetting("deviceid")

		connection = httplib.HTTPConnection(hostname,port)
		connection.connect()
		if switchOn:
			url = "/device/on/%s" % deviceid
		else:
			url = "/device/off/%s" % deviceid

		connection.request("GET", url)

	def execute(self):
		monitor = xbmc.Monitor()
		while True:
			if monitor.waitForAbort(10):
				break



# Main ----------------------------------------------
anna = Anna()
anna.execute()