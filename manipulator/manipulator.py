import time
import datetime
import socket

port = 65200
m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # m.connect(('127.0.0.1',port))
    m.connect(('172.17.0.2',port))
except socket.error as e:
    print("Error: ",e)


class manipulator:

    def receive(self, date_time, status):               
        return({'datetime':  date_time, 'status': status})

    def logger(self, update):
        print('controller status')
        print(self.receive('{:%Y-%m-%d %H:%M}'.
            format(datetime.datetime.today()),update))

    def status(self):
        print('manipulator status')

mani = manipulator()

while True:
    
    msg = m.recv(1024)
    if msg:        
        print(msg.decode('utf-8'),"\n")
        # mani.logger(stat) 
    else:
        print('No msg received!')   
    # time.sleep(5)