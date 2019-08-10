from datetime import datetime,timedelta
import re

class Minute:

	@classmethod
	def start_of(cls, mtime):
		return mtime.replace(second=0, microsecond=0)

	@classmethod
	def add(cls, mtime, val):
		return mtime + timedelta(minutes=val)

	@classmethod
	def subtract(cls, mtime, val):
		return mtime - timedelta(minutes=val)

class Hour:

	@classmethod
	def start_of(cls, mtime):
		return mtime.replace(minute=0, second=0, microsecond=0)

	@classmethod
	def add(cls, mtime, val):
		return mtime + timedelta(hours=val)

	@classmethod
	def subtract(cls, mtime, val):
		return mtime - timedelta(hours=val)

class Day:

	@classmethod
	def start_of(cls, mtime):
		return mtime.replace(hour=0, minute=0, second=0, microsecond=0)

	@classmethod
	def add(cls, mtime, val):
		return mtime + timedelta(days=val)

	@classmethod
	def subtract(cls, mtime, val):
		return mtime - timedelta(days=val)

class Samay:

	def __init__(self, mtime=None):
		if mtime == None:
			self.mtime = datetime.now()
		else:
			self.mtime = mtime
		if not self.mtime:
			raise Exception("Argument must be an instance of date time.")

	@classmethod
	def from_int(cls, mtime):
		try:
			if len(str(mtime)) > 10:
				mtime = mtime//1000
			return cls(datetime.fromtimestamp(mtime))
		except:
			print("Argument must be of EPOC time.")

	@classmethod
	def from_str(cls, mtime):
		try:
			f_mtime = mtime.split(":")
			if len(f_mtime) == 2:
				mtime = datetime.strptime(mtime, "%Y-%m-%d %H:%M")
			else:
				mtime = datetime.strptime(mtime, "%Y-%m-%d %H:%M:%S")
			return cls(mtime)
		except:
			print("Argument must be of format YYYY-MM-DD HH:mm:ss or YYYY-MM-DD HH:mm")

	def start_of(self, arg):
		unit = self.get_time_unit(arg)
		self.mtime = unit.start_of(self.mtime)
		return self

	def add(self, val, _type):
		unit = self.get_time_unit(_type)
		self.mtime = unit.add(self.mtime, val)
		return self

	def subtract(self, val, _type):
		unit = self.get_time_unit(_type)
		self.mtime = unit.subtract(self.mtime, val)
		return self

	def get_time_unit(self, arg):
		if arg == "min":
			return Minute
		if arg == "hour":
			return Hour
		if arg == "day":
			return Day

	def format(self,strArg):
		strArg = str(strArg)
		strArg = strArg.replace("YYYY","%Y")
			.replace("DD","%d")
			.replace("dd","%d")
			.replace("mm","%M")
			.replace("MM","%m")
			.replace("ss","%S")
			.replace("hh","%H")
			.replace("HH","%H")
		return self.mtime.strftime(strArg)

	def __str__(self):
		return str(self.mtime.format("YYYY-MM-DD HH:mm"))

	def unix(self):
		return int(self.mtime.strftime("%s"))*1000

	def __gt__(self,other):
		return self.mtime > other.mtime

	def __eq__(self,other):
		return self.mtime == other.mtime
	def __lt__(self,other):
		return self.mtime < other.mtime