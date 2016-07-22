import config
import streamopener
import os.path as path
import player
import application
import wx
class MainGui(wx.Frame):
	def __init__(self, title):
		wx.Frame.__init__(self, None, title=title, size=(350,200)) # initialize the wx frame
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.panel = wx.Panel(self)
		self.main_box = wx.BoxSizer(wx.VERTICAL)

		self.menuBar = wx.MenuBar()
		menu = wx.Menu()
		m_open = menu.Append(-1, "Open\tControl-O", "")
		self.Bind(wx.EVT_MENU, self.open, m_open)
		m_add = menu.Append(-1, "Add song to playlist\tControl+Shift+O", "")
		self.Bind(wx.EVT_MENU, self.add, m_add)
		m_stream = menu.Append(-1, "Open Audio Stream\tControl-U", "")
		self.Bind(wx.EVT_MENU, self.stream, m_stream)
		m_save = menu.Append(-1, "Save playlist\tControl+S", "")
		self.Bind(wx.EVT_MENU, self.save, m_save)
		m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
		self.Bind(wx.EVT_MENU, self.OnClose, m_exit)
		self.menuBar.Append(menu, "&File")
		menu = wx.Menu()
		m_play = menu.Append(-1, "Play/pause\tSpace", "")
		self.Bind(wx.EVT_MENU, self.play, m_play)
		m_previous = menu.Append(-1, "Previous track\tControl+Left arrow", "")
		self.Bind(wx.EVT_MENU, self.previous, m_previous)
		m_next = menu.Append(-1, "Next track\tControl+Right arrow", "")
		self.Bind(wx.EVT_MENU, self.next, m_next)
		m_volup = menu.Append(-1, "Increase Volume\tUp arrow", "")
		self.Bind(wx.EVT_MENU, self.volup, m_volup)
		m_voldown = menu.Append(-1, "Decrease Volume\tDown arrow", "")
		self.Bind(wx.EVT_MENU, self.voldown, m_voldown)
		m_seekleft = menu.Append(-1, "Seek back 5 seconds\tLeft arrow", "")
		self.Bind(wx.EVT_MENU, self.seekleft, m_seekleft)
		m_seekleft2 = menu.Append(-1, "Seek back 15 seconds\tShift+Left arrow", "")
		self.Bind(wx.EVT_MENU, self.seekleft2, m_seekleft2)
		m_seekleft3 = menu.Append(-1, "Seek back 30 seconds\tControl+Shift+Left arrow", "")
		self.Bind(wx.EVT_MENU, self.seekleft3, m_seekleft3)
		m_seekleft4 = menu.Append(-1, "Seek back 1 minute\tAlt+Left arrow", "")
		self.Bind(wx.EVT_MENU, self.seekleft4, m_seekleft4)
		m_seekright = menu.Append(-1, "Seek forward 5 seconds\tRight arrow", "")
		self.Bind(wx.EVT_MENU, self.seekright, m_seekright)
		m_seekright2 = menu.Append(-1, "Seek forward 15 seconds\tShift+Right arrow", "")
		self.Bind(wx.EVT_MENU, self.seekright2, m_seekright2)
		m_seekright3 = menu.Append(-1, "Seek forward 30 seconds\tControl+Shift+Right arrow", "")
		self.Bind(wx.EVT_MENU, self.seekright3, m_seekright3)
		m_seekright4 = menu.Append(-1, "Seek forward 1 minute\tAlt+Right arrow", "")
		self.Bind(wx.EVT_MENU, self.seekright4, m_seekright4)
		self.menuBar.Append(menu, "&Transport")
		menu = wx.Menu()
		m_set = menu.Append(-1, "Speak elapsed time\tControl+Shift+e", "")
		self.Bind(wx.EVT_MENU, self.set, m_set)
		m_srt = menu.Append(-1, "Speak remaining time\tControl+Shift+R", "")
		self.Bind(wx.EVT_MENU, self.srt, m_srt)
		m_sl = menu.Append(-1, "Speak length\tControl+Shift+T", "")
		self.Bind(wx.EVT_MENU, self.sl, m_sl)
		self.menuBar.Append(menu, "&Accessibility")
		self.SetMenuBar(self.menuBar)
		accel=[]
		accel.append((wx.ACCEL_CTRL, ord('O'), m_open.GetId()))
		accel.append((wx.ACCEL_CTRL|wx.ACCEL_SHIFT, ord('O'), m_add.GetId()))
		accel.append((wx.ACCEL_CTRL, ord('U'), m_stream.GetId()))
		accel.append((wx.ACCEL_CTRL, ord('S'), m_save.GetId()))
		accel.append((wx.ACCEL_NORMAL, ord(' '), m_play.GetId()))
		accel.append((wx.ACCEL_NORMAL, ord('c'), m_play.GetId()))
		accel.append((wx.ACCEL_NORMAL, wx.WXK_LEFT, m_seekleft.GetId()))
		accel.append((wx.ACCEL_SHIFT, wx.WXK_LEFT, m_seekleft2.GetId()))
		accel.append((wx.ACCEL_CTRL|wx.ACCEL_SHIFT, wx.WXK_LEFT, m_seekleft3.GetId()))
		accel.append((wx.ACCEL_ALT, wx.WXK_LEFT, m_seekleft4.GetId()))
		accel.append((wx.ACCEL_NORMAL, wx.WXK_RIGHT, m_seekright.GetId()))
		accel.append((wx.ACCEL_SHIFT, wx.WXK_RIGHT, m_seekright2.GetId()))
		accel.append((wx.ACCEL_CTRL|wx.ACCEL_SHIFT, wx.WXK_RIGHT, m_seekright3.GetId()))
		accel.append((wx.ACCEL_ALT, wx.WXK_RIGHT, m_seekright4.GetId()))
		accel.append((wx.ACCEL_CTRL, wx.WXK_LEFT, m_previous.GetId()))
		accel.append((wx.ACCEL_CTRL, wx.WXK_RIGHT, m_next.GetId()))
		accel.append((wx.ACCEL_NORMAL, wx.WXK_UP, m_volup.GetId()))
		accel.append((wx.ACCEL_NORMAL, wx.WXK_DOWN, m_voldown.GetId()))
		accel.append((wx.ACCEL_CTRL|wx.ACCEL_SHIFT, ord('R'), m_srt.GetId()))
		accel.append((wx.ACCEL_CTRL|wx.ACCEL_SHIFT, ord('E'), m_set.GetId()))
		accel.append((wx.ACCEL_CTRL|wx.ACCEL_SHIFT, ord('T'), m_sl.GetId()))
		self.panel.Layout()
		accel_tbl=wx.AcceleratorTable(accel)
		self.SetAcceleratorTable(accel_tbl)

	def previous(self,event):
		if player.p.loaded==True:
			player.switchtrack(-1)

	def next(self,event):
		if player.p.loaded==True:
			player.switchtrack(1)

	def srt(self,event):
		if player.p.loaded==True:
			player.speak_remaining_time()

	def set(self,event):
		if player.p.loaded==True:
			player.speak_elapsed_time()

	def sl(self,event):
		if player.p.loaded==True:
			player.speak_length()

	def open(self,event):
		openFileDialog = wx.FileDialog(self, "Select the audio file to be opened", "", "", "Audio Files (*.mp3, *.ogg, *.flac, *.wav, *.opus, *.m4a, *.wma, *.m3u)|*.mp3; *.ogg; *.wav; *.opus; *.m4a; *.wma; *.flac; *.m3u", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		if openFileDialog.ShowModal() == wx.ID_CANCEL:
			return False
		self.filename= openFileDialog.GetPath()
		self.name=path.basename(self.filename)
		player.p.songs=[]
		if ".m3u" in self.filename:
			player.open_playlist(self.filename,self.filename.replace(self.name,""))
		else:
			player.p.songs.append(self.filename)
			player.p.songindex=0
			player.open_file(self.filename,self.name)

	def add(self,event):
		openFileDialog = wx.FileDialog(self, "Select the audio file to be added", "", "", "Audio Files (*.mp3, *.ogg, *.flac, *.wav, *.opus, *.m4a, *.wma)|*.mp3; *.ogg; *.wav; *.opus; *.m4a; *.wma; *.flac", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		if openFileDialog.ShowModal() == wx.ID_CANCEL:
			return False
		self.filename= openFileDialog.GetPath()
		self.name=path.basename(self.filename)
		player.add_file(self.filename,self.name)

	def save(self,event):
		openFileDialog = wx.FileDialog(self, "Select the destination playlist file to save", "", "", "playlist (*.m3u)|*.m3u", wx.FD_SAVE )
		if openFileDialog.ShowModal() == wx.ID_CANCEL:
			return False
		self.filename= openFileDialog.GetPath()
		self.path=self.filename.replace(path.basename(self.filename),"")
		player.save_playlist(self.path,path.basename(self.filename))

	def stream(self,event):
		inp=streamopener.Input("Open Audio Stream","Enter a URL to an Audio Stream")
		inp.Show()

	def volup(self,event):
		if player.p.loaded==True:
			if player.p.handle.volume<1.0:
				try:
					player.p.handle.volume+=0.02
				except:
					pass
		config.appconfig['general']['volume']=round(player.p.handle.volume,2)
		config.appconfig.write()

	def voldown(self,event):
		if player.p.loaded==True:
			if player.p.handle.volume>0.0:
				try:
					player.p.handle.volume-=0.02
				except:
					pass
		config.appconfig['general']['volume']=round(player.p.handle.volume,1)
		config.appconfig.write()

	def seekleft(self,event):
		if player.p.loaded==True:
			player.seek(-5)

	def seekleft2(self,event):
		if player.p.loaded==True:
			player.seek(-15)

	def seekleft3(self,event):
		if player.p.loaded==True:
			player.seek(-30)

	def seekleft4(self,event):
		if player.p.loaded==True:
			player.seek(-60)

	def seekright(self,event):
		if player.p.loaded==True:
			player.seek(5)

	def seekright2(self,event):
		if player.p.loaded==True:
			player.seek(15)

	def seekright3(self,event):
		if player.p.loaded==True:
			player.seek(30)

	def seekright4(self,event):
		if player.p.loaded==True:
			player.seek(60)

	def play(self, event):
		if player.p.loaded==True and player.p.streaming==False:
			if player.p.handle.is_playing==False:
				player.play()
			else:
				player.pause()

	def OnClose(self, event):
		"""App close event handler"""
		self.Destroy()
global window
window=MainGui(application.name+" V"+application.version)