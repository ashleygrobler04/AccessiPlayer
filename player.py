import config
import timefuncs
from speech import speak
import sound_lib
from sound_lib import output
from sound_lib import stream
from sound_lib.effects import effect
from sound_lib.effects import tempo
class status(object):
	def __init__(self):
		self.loaded=False
		self.streaming=False
		self.songindex=0
		self.songs=[]
		self.handle=0
		self.tempo=0

filename=""
p=status()
o=output.Output()

def open_file(filen="",fn=""):
	p.handle =stream.FileStream(file=filen)
	filename=fn
	p.streaming=False
	p.loaded=True
#	p.tempo=tempo.Tempo(p.handle.handle)
	p.handle.volume=config.appconfig['general']['volume']

def add_file(filen="",fn=""):
	p.songs.append(filen)

def open_playlist(filename,path):
	f=open(filename,"r")
	data=f.read()
	f.close()
	songs=data.split("\n")
	for i in range(0,len(songs)):
		songs[i]=songs[i].replace("\r","")
		if "http://" in songs[i]==False:
			try:
				f=open(songs[i],"r")
				f.close()
			except:
				songs[i]=path+songs[i]
	p.songs=songs
	switchtrack(0)

def open_stream(filen=""):
	p.handle =stream.URLStream(url=filename)
	p.streaming=True
	p.loaded=True
	p.songindex=0
	play()

def play():
	if not p.handle==0:
		p.handle.play()

def stop():
	if not p.handle==0:
		p.handle.stop()
		p.handle.set_position(0)
def pause():
	if not p.handle==0:
		p.handle.pause()

def seek(step):
	pos=p.handle.get_position()
	pos=p.handle.bytes_to_seconds(pos)
	pos+=step
	pos=p.handle.seconds_to_bytes(pos)
	if pos<0:
		pos=0
	p.handle.set_position(pos)

def speak_remaining_time():
	pos=p.handle.get_position()
	pos2=p.handle.get_length()
	pos=p.handle.bytes_to_seconds(pos)
	pos2=p.handle.bytes_to_seconds(pos2)
	speak(timefuncs.grt((pos2*1000)-(pos*1000)))

def speak_elapsed_time():
	pos=p.handle.get_position()
	pos=p.handle.bytes_to_seconds(pos)
	speak(timefuncs.grt(pos*1000))

def speak_length():
	pos=p.handle.get_length()
	pos=p.handle.bytes_to_seconds(pos)
	speak(timefuncs.grt(pos*1000))

def switchtrack(step):
	p.songindex+=step
	if p.songindex<0 or p.songindex>=len(p.songs):
		p.songindex=0
	s=p.songs[p.songindex].split(":")
	try:
		playing=p.handle.is_playing
	except:
		playing=False

	if s[0]=="http":
		open_stream(p.songs[p.songindex])
	else:
		open_file(p.songs[p.songindex])
	if playing==True:
		play()

def save_playlist(path, filename):
	files=""
	f=open(path+filename,"w")
	for i in range(0,len(p.songs)):
		p.songs[i]=p.songs[i].replace(path,"")
		files+=p.songs[i]+"\n"
	f.write(files)
	f.close()