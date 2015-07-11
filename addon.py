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

def getAdress():
	ipaddress = __settings__.getSetting("ipaddress")
	port = __settings__.getSetting("port")
	deviceid = __settings__.getSetting("deviceid")
	return "http://%s:%s/device/%s" % (ipaddress, port, deviceid)

def request(adress, switchOn):
	if switchOn:
		adress = adress + "/1"
	else:
		adress = adress + "/0"

	h = httplib2.Http()
	h.request(adress, "GET")

def switchOn():
	adress = getAdress()
	request(adress, True)

def switchOff():
	adress = getAdress()
	request(adress, False)



while True:
	if monitor.waitForAbort(10):
		break