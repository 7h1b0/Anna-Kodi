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
			deviceid_off = settings.getSetting("deviceid_start_on")
			self.request(deviceid_off, True)
			deviceid_on = settings.getSetting("deviceid_start_off")
			self.request(deviceid_on, False)

	def onPlayBackPaused(self):
		deviceid_on = settings.getSetting("deviceid_pause_on")
		self.request(deviceid_on,True)
		deviceid_off = settings.getSetting("deviceid_pause_off")
		self.request(deviceid_off,False)

	def onPlayBackResumed(self):
		deviceid_on = settings.getSetting("deviceid_resume_on")
		self.request(deviceid_on,True)
		deviceid_off = settings.getSetting("deviceid_resume_off")
		self.request(deviceid_off,False)

	def onPlayBackEnded(self):
		if playlist.size() == playlist.getposition() + 1:
			deviceid_on = settings.getSetting("deviceid_end_on")
			self.request(deviceid_on, True)
			deviceid_off = settings.getSetting("deviceid_end_off")
			self.request(deviceid_off, False)

	def onPlayBackStopped(self):
		deviceid_on = settings.getSetting("deviceid_stop_on")
		self.request(deviceid_on, True)
		deviceid_off = settings.getSetting("deviceid_stop_off")
		self.request(deviceid_off, False)

	def request(self,deviceid, switchOn):
		if deviceid == 0 :
			return
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