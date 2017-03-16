import time
import sys
import config
import player
import wx
app = wx.App(redirect=False)
from gui import interface
config.setup()
interface.window.Show()

if config.appconfig['general']['resumelastsong']==True and config.appconfig['general']['lastsong']!="":
	try:
		player.open_file(config.appconfig['general']['lastsong'])
		player.p.stream.set_position(int(config.appconfig['general']['lastsongposition']))
		player.play()
	except:
		config.appconfig['general']['lastsong']=""
		config.appconfig['general']['lastsongposition']=0

app.MainLoop()