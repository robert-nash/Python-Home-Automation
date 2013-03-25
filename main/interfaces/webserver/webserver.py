import time
import cherrypy

def run(update,register,getstate,getdevices):  
        cherrypy.config.update({'server.socket_host': '0.0.0.0'})
        cherrypy.quickstart(handler(update,getstate,getdevices))
class handler(object):
    def __init__(self, update,getstate,getdevices):
        self.update = update
        self.getstate = getstate
        self.getdevices = getdevices
    def index(self):
        devices = self.getdevices()
        response = ''
        for f in devices:
            response += f + ' ' + self.getstate(f)
        return response
    def updatedevice(self,name,state):
        self.update(name,state)
        return name + ' ' + state
    updatedevice.exposed = True
    index.exposed = True
    