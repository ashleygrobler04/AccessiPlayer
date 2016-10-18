import player
import wx
global value
value=""
class Input(wx.Frame):
	def __init__(self, title,text):
		wx.Frame.__init__(self, None, title=title, size=(350,200)) # initialize the wx frame
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)
		self.text_label = wx.StaticText(self.panel, -1, text)
		self.text = wx.TextCtrl(self.panel, -1, "",style=wx.TE_MULTILINE)
		self.main_box.Add(self.text, 0, wx.ALL, 10)
		self.ok = wx.Button(self.panel, wx.ID_OK, "&OK")
		self.ok.Bind(wx.EVT_BUTTON, self.OnOK)
		self.main_box.Add(self.ok, 0, wx.ALL, 10)
		self.close = wx.Button(self.panel, wx.ID_CLOSE, "&Cancel")
		self.close.Bind(wx.EVT_BUTTON, self.OnClose)
		self.main_box.Add(self.close, 0, wx.ALL, 10)
		self.panel.Layout()

	def OnClose(self, event):
		self.Destroy()

	def OnOK(self, event):
		value=self.text.GetValue()
		player.open_stream(value)
		self.Destroy()
