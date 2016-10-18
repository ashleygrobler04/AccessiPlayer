import os, sys
import config
import wx
class OptionsGui(wx.Frame):

	def __init__(self):

		self.ws=config.appconfig['general']['resumelastsong']
		wx.Frame.__init__(self, None, title="Options", size=(350,200)) # initialize the wx frame
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)
		self.lastsong = wx.CheckBox(self.panel, -1, "&Resume last played item on startup")
		self.main_box.Add(self.lastsong, 0, wx.ALL, 10)
		self.lastsong.SetValue(self.ws)
		self.ok = wx.Button(self.panel, wx.ID_OK, "&OK")
		self.ok.Bind(wx.EVT_BUTTON, self.OnOK)
		self.main_box.Add(self.ok, 0, wx.ALL, 10)
		self.close = wx.Button(self.panel, wx.ID_CLOSE, "&Cancel")
		self.close.Bind(wx.EVT_BUTTON, self.OnClose)
		self.main_box.Add(self.close, 0, wx.ALL, 10)
		self.panel.Layout()

	def OnOK(self, event):
		config.appconfig['general']['resumelastsong']=self.lastsong.GetValue()
		config.appconfig.write()
		self.Destroy()

	def OnClose(self, event):
		self.Destroy()