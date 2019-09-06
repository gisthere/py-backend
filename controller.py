#! usr/bin python3

import socket
port = 65455

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), port))
s.listen(8)

class controller:
	""" A controller class"""
	sensors = 8
	packets = 100

	def active_sensor(elsf,sen):
		sensors = sen
		return sensors

	def send_packet(self,pack):
		packets = pack
		return packets

test = controller()
print(test.__doc__)
print('number of sensors: ',test.active_sensor(7))
print('packets delivered: ', test.send_packet(94))
print(test.sensors)
print(socket.gethostname())

while True:
	clientsocket, address = s.accept()
	print(f'Connection from {address} is establihed!')
	clientsocket.send(bytes('This is the controller socket', 'utf-8'))

