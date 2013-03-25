from threading import Thread
import importlib
import interfaces

modules = ['webserver','interface',]
devices = {'tes':{
                  'type': 'light',
                  'state':'ON',
                  'notify': []
                  }
           }

def clients():
    def interface():
        for f in modules:
            module = importlib.import_module('interfaces.'+f+'.'+f)            
            Thread(target=module.run, args=([update,register,getstate,getdevices])).start()   
    interface()
def notify(name):
    for f in devices[name]['notify']:
        Thread(target=f, args=([update,register,getstate,name])).start()  
def update(name,state):
    devices[name]['state'] = state
    notify(name)
def getstate(name):
    return devices[name]['state']   
def getdevices(): 
    returndevices = []
    for f in devices.keys():   
        returndevices.append(f)
    return returndevices
def register(notify,devicetype):    
    for f in devices.keys():        
        if devices[f]['type'] == devicetype:            
            devices[f]['notify'].append(notify)
clients()
#Thread(target=clients, args=()).start()