from threading import Thread
import threading
from handler.HandlerRequests import HandlerRequests 
import _thread
import time
from datetime import datetime, timezone
from entities.User import User
from random import randint

class HandlerConnections(Thread):
    def __init__(self, server):
        Thread.__init__(self)
        self.server = server

    def run(self):
        while True:
            connectionSocket, addr = self.server.serverSocket.accept()

            connectionSocket.send( ("Seja bem vindo ao concord!\n\nDeseja se registrar ou logar?\n"
                                            + "Para logar execute '/login <user> <passw>' \n"
                                            + "Para registrar execute '/register <name> <user> <passw>' \n\n").encode() )

            user = User("UserRandom", "random" + str(randint(0, 10000)), "", connectionSocket)
            
            self.server.activeUser.append(connectionSocket)
            t = HandlerRequests(connectionSocket, self.server, user)
            t.start()  
