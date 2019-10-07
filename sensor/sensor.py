
import datetime
import random
import time

class sensor: # <--- problem with code style. It's not pep8.
	def __init__(self, datetime, payload):
		self.datetime = datetime
		self.payload = payload
	
	def date(self):
		date_time = datetime.datetime.today()
		self.datetime = '{:%Y-%m-%d %H:%M}'.format(date_time)
		return {self.datetime} #

	def data(self):
		x = random.randint(1,100)
		return x

	def signal(self):
		self.datetime = self.date()
		self.payload = self.data()
		return {'datetime' : self.datetime, 'payload' : self.payload}

	def sensors_signal(self):
		sensors = range(8)
		info = []
		for s in sensors:
			s = sensor('2019-01-01:00:00',0) #  <--- overriding variable which is used in loop
			info.append(s.signal())
			sig = str(info).encode('ASCII') #  <--- using ascii instead utf
		return sig

if __name__ == "__main__": #  <--- it's not clear purpose of this code. Need more comments or documentation.
	while True:
		s1 = sensor('2000-01-01:00:00',100)
		time.sleep(1)
		print(s1.sensors_signal(),"\n")
