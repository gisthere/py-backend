import time
import datetime
import socket

port = 65455

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('hostname: ',socket.gethostname())
s.connect(('172.17.0.2',port))

msg = s.recv(1024)
print(msg.decode('utf-8'))

class manipulator:

    def receive(self, date_time, status):               
        return({'datetime':  date_time, 'status': status})

    def logger(self):
        print('Logs from controller')
        print(self.receive('{:%Y-%m-%d %H:%M}'.
            format(datetime.datetime.today()),['up','dowm']))

    def status(self):
        print('manipulator status')

m = manipulator()

while time:
    m.logger()    
    time.sleep(5)