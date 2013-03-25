from threading import Thread
import time
import serial

ser = serial.Serial('/dev/ttyAMA0', 9600)

def run(update,register,getstate,getdevices):  
    register(write,'light')
    Thread(target=read, args=([update])).start()   
    
def read(update):
    serial = False
    while 1:
        if serial:
            update('tes','OFF')
        time.sleep(1)
def write(update,register,getstate,name):
    ser.write(name+' '+getstate(name)+'\n')
    print name
    print getstate(name)
    