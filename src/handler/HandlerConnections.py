from threading import Thread
import threading
from handler.HandlerRequests import HandlerRequests 
import _thread
import time
from datetime import datetime, timezone

class HandlerConnections(Thread):
    def __init__(self, server):
        Thread.__init__(self)
        self.server = server

    def run(self):
        while True:
            connectionSocket, addr = self.server.serverSocket.accept()
            
            self.server.activeUser.append(connectionSocket)
            t = HandlerRequests(connectionSocket, self.server)
            t.start()  
