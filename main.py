import time
import sys
import config
import player
import wx
app = wx.App(redirect=False)
from gui import interface
config.setup()
interface.window.Show()

try:
	args=str(sys.argv[1])
except:
	args=str(sys.argv[0])
	if args=="main.py":
		args=""

if config.appconfig['general']['resumelastsong']==True and config.appconfig['general']['lastsong']!="" and args=="":
	player.open_file(config.appconfig['general']['lastsong'])
	player.p.stream.set_position(int(config.appconfig['general']['lastsongposition']))
	player.play()

elif args!="":
	speak(args)
	time.sleep(1)
	player.open_file(args)
	player.play()

app.MainLoop()