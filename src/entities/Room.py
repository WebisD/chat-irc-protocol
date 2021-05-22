import socket 
import select 
import sys 
import _thread
from entities.User import User

class Room:
    def __init__(self, name, maxUser):
        self.name = name
        self.list_of_clients = [] 
        self.maxUser = maxUser

    def clientthread(self, user, message): 
        # sends a message to the client whose user object is conn 
        user.connectionSkt.send(message.encode()) 
    
    """Using the below function, we broadcast the message to all 
    clients who's object is not the same as the one sending 
    the message """
    def broadcast(self, message, user): 
        for clients in self.list_of_clients: 
            if clients.connectionSkt!=user.connectionSkt: 
                try: 
                    clients.connectionSkt.send((message + "\n").encode()) 
                except: 
                    clients.connectionSkt.close() 
    
                    # if the link is broken, we remove the client 
                    self.remove(clients) 
            else:
                user.connectionSkt.send(("you said: " + message + "\n").encode())
    
    """The following function simply removes the object 
    from the list that was created at the beginning of 
    the program"""
    def remove(self, user): 
        if user in self.list_of_clients: 
            self.list_of_clients.remove(user) 
    
    def add(self, user: User): 
        if (len(self.list_of_clients) + 1) <= self.maxUser:
            if user not in self.list_of_clients: 
                self.list_of_clients.append(user)
            print(self.list_of_clients)
            #self.broadcast("Entrou na sala " + str(user.name), user)
            user.connectionSkt.send(("Welcome to " + self.name + "!\n\n").encode())  
            return True 
        
        return False