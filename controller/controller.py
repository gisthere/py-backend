
import time
import threading
import datetime
import socket
import asyncio
import sys
sys.path.append(".")


class controller:
	""" A controller class"""
	sensors = 8
	packets = 100
	status = 'down'

	def active_sensor(elsf,sen):
		sensors = sen
		return sensors

	async def timer(self):
		time.sleep(1)		
		

	def update(self):		
		threading.Timer(5.0, self.update).start()
		status = {'datetime':'{:%Y-%m-%d %H:%M}'.format(datetime.datetime.today()),'status':'up'}
		print(status)
		return str(status).encode('ASCII')

c = controller()

print(c.__doc__)
loop = asyncio.get_event_loop()
loop.run_until_complete(c.timer()) #  <--- useless code

# sen.connect(('172.17.0.3',port2))

port1 = 65200
contr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
contr.bind((socket.gethostname(), port1))
contr.listen(1)
manip, manip_addr = contr.accept()

try:
	from sensor.sensor import * #  <--- 1. why import two times?
	s1 = sensor('2019-01-01:00:00',0)
except ImportError:
    from .sensor.sensor import * #  <--- 2.

# controller_update = c.update()
c.update()

while True:
	msg = s1.sensors_signal()
	# manip.send(str(c.update()).encode('ascii'))
	if manip:
		manip.send(msg)		
		time.sleep(1)
	else:
		print('Manipulator is down or disconnected!')
	