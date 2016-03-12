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
		self.request("start")

	def onPlayBackPaused(self):
		self.request("pause")

	def onPlayBackResumed(self):
		self.request("resume")

	def onPlayBackEnded(self):
		if playlist.size() == playlist.getposition() + 1:
			self.request("ended")

	def onPlayBackStopped(self):
		self.request("stop")

	def request(self, action):
		hostname = settings.getSetting("hostname")
		port = settings.getSetting("port")

		connection = httplib.HTTPConnection(hostname, port)
		token = settings.getSetting("token")
		url = "/api/kodi/%s" % action

		connection.putrequest("GET", url)
		connection.putheader("x-access-token", token)
		connection.endheaders()

	def execute(self):
		monitor = xbmc.Monitor()
		while True:
			if monitor.waitForAbort(10):
				break



# Main ----------------------------------------------
anna = Anna()
anna.execute()