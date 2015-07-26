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
			deviceid = settings.getSetting("deviceid_start")
			self.request(deviceid, False)

	def onPlayBackPaused(self):
		deviceid = settings.getSetting("deviceid_pause")
		self.request(deviceid,True)

	def onPlayBackResumed(self):
		deviceid = settings.getSetting("deviceid_resume")
		self.request(deviceid,False)

	def onPlayBackEnded(self):
		if playlist.size() == playlist.getposition() + 1:
			deviceid = settings.getSetting("deviceid_end")
			self.request(True)

	def onPlayBackStopped(self):
		deviceid = settings.getSetting("deviceid_stop")
		self.request(deviceid, True)

	def request(self,deviceid, switchOn):
		hostname = settings.getSetting("hostname")
		port = settings.getSetting("port")

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