import xbmc
import xbmcaddon
import httplib2

__settings__  = xbmcaddon.Addon(id="service.kodi.anna")
 
class XBMCPlayer(xbmc.Player):
	def __init__(self, *args):
		pass

	def onPlayBackStarted(self):
		switchOff()

	def onPlayBackPaused(self):
		switchOn()

	def onPlayBackResumed(self):
		switchOff()

	def onPlayBackEnded(self):
		switchOn()

	def onPlayBackStopped(self):
		switchOn()

player = XBMCPlayer()
monitor = xbmc.Monitor()
h = httplib2.Http()

def getAdress(switchOn):
	ipaddress = __settings__.getSetting("ipaddress")
	port = __settings__.getSetting("port")
	deviceid = __settings__.getSetting("deviceid")
	if switchOn:
		return "http://%s:%s/device/on/%s" % (ipaddress, port, deviceid)
	else:
		return "http://%s:%s/device/off/%s" % (ipaddress, port, deviceid)

def request(switchOn):
	adress = getAdress(switchOn)

	h = httplib2.Http()
	h.request(adress, "GET")

def switchOn():
	request(True)

def switchOff():
	request(False)



while True:
	if monitor.waitForAbort(10):
		break