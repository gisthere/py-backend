#! /usr/bin python3
import datetime
import random
import numpy as np
import time

class sensor:

	def __init__(self, datetime, payload):
		self.datetime = datetime
		self.payload = payload
	
	def date(self):
		date_time = datetime.datetime.today()
		self.datetime = '{:%Y-%m-%d %H:%M}'.format(date_time)
		return {self.datetime}

	def data(self):
		x = random.randint(1,100)
		return x

	def signal(self):
		self.datetime = self.date()
		self.payload = self.data()
		return {'datetime' : self.datetime, 'payload' : self.payload}


def sensors_signal():
	sensors = np.ndarray(8,bytes)
	info = []
	for s in sensors:
		s = sensor('2019-01-01:00:00',0)		
		info.append(s.signal())
	return info

while time:
	print(sensors_signal())
	time.sleep(5)
	


# def set_interval(func, sec):
# 	def func_wrapper():
# 		set_interval(func, sec) 
# 		func
# 	t = threading.Timer(sec, func_wrapper)
# 	t.start()
# 	return func_wrapper()
