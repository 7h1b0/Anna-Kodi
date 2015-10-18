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
		# if playlist.getposition() == 0:
		sceneId = settings.getSetting("sceneid_on_start")
		self.request(sceneId)

	def onPlayBackPaused(self):
		sceneId = settings.getSetting("sceneid_on_pause")
		self.request(sceneId)

	def onPlayBackResumed(self):
		sceneId = settings.getSetting("sceneid_on_resume")
		self.request(sceneId)

	def onPlayBackEnded(self):
		if playlist.size() == playlist.getposition() + 1:
			sceneId = settings.getSetting("sceneid_on_end")
			self.request(sceneId)

	def onPlayBackStopped(self):
		sceneId = settings.getSetting("sceneid_on_stop")
		self.request(sceneId)

	def request(self,sceneId):
		if sceneId == 0 :
			return
		hostname = settings.getSetting("hostname")
		port = settings.getSetting("port")

		print(hostname)
		connection = httplib.HTTPConnection(hostname,port)
		connection.connect()
		url = "/scene/%s/action" % sceneId

		connection.request("GET", url)

	def execute(self):
		monitor = xbmc.Monitor()
		while True:
			if monitor.waitForAbort(10):
				break



# Main ----------------------------------------------
anna = Anna()
anna.execute()