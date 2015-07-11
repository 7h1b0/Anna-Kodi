import xbmc
import httplib2
 
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

def switchOn():
	h.request("http://192.168.1.11:8080/device/2/1", "GET")

def switchOff():
	h.request("http://192.168.1.11:8080/device/2/0", "GET")

while True:
	if monitor.waitForAbort(10):
		break