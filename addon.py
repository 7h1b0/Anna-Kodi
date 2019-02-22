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

	def onAVStarted(self):
		alias = settings.getSetting("onStart")
		self.request(alias)

	def onPlayBackPaused(self):
		alias = settings.getSetting("onPause")
		self.request(alias)

	def onPlayBackResumed(self):
		alias = settings.getSetting("onResume")
		self.request(alias)

	def onPlayBackEnded(self):
		if playlist.size() == playlist.getposition() + 1:
			alias = settings.getSetting("onEnd")
			self.request(alias)

	def onPlayBackStopped(self):
		alias = settings.getSetting("onStop")
		self.request(alias)

	def request(self, alias):
		hostname = settings.getSetting("hostname")
		port = settings.getSetting("port")

		connection = httplib.HTTPConnection(hostname, port)
		token = settings.getSetting("token")
		url = "/api/alias/%s/action" % alias

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