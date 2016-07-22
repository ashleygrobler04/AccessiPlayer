import config
import player
import wx
app = wx.App(redirect=False)
from gui import interface
config.setup()
interface.window.Show()
app.MainLoop()