import math
def grt(milliseconds):
	milliseconds=math.floor(milliseconds)
	seconds=math.floor((milliseconds/1000)%60)
	minutes=math.floor(((milliseconds/(1000*60))%60))
	hours=math.floor(((milliseconds/(1000*60*60))%24))
	days=int(milliseconds/1000/60/60/24)
	days=math.floor(days)
	hours=math.floor(hours)
	minutes=math.floor(minutes)
	seconds=math.floor(seconds)
	this1=""
	if days>0:
		this1=str(int(days))+":"
	this2=""
	if hours>0:
		if hours<=9 and hours>0:
			this2="0"+str(int(hours))+":"
		else:
			this2=str(int(hours))+":"

	this3=""
	if minutes>0:
		if minutes<=9 and minutes>0:
			this3="0"+str(int(minutes))+":"
		else:
			this3=str(int(minutes))+":"

	if seconds<=9:
		this4="0"+str(int(seconds))
	else:
		this4=str(int(seconds))

	return this1+this2+this3+this4