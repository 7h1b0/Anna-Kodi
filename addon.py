# Imports -----------------------------------------------
import xbmc, xbmcaddon
import httplib


# Settings -----------------------------------------------
settings  = xbmcaddon.Addon(id="service.kodi.anna")

# Playlist -----------------------------------------------
playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
 

# Classes ------------------------------------------------
class Anna(xbmc.Player):
	def __init__(self, *args):
		pass

	def onPlayBackStarted(self):
		if playlist.getposition() == 0:
			self.request(False)

	def onPlayBackPaused(self):
		self.request(True)

	def onPlayBackResumed(self):
		self.request(False)

	def onPlayBackEnded(self):
		if playlist.size() == playlist.getposition() + 1:
			self.request(True)

	def onPlayBackStopped(self):
		self.request(True)

	def request(self,switchOn):
		xbmc.log("Request done")
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