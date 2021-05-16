import socket 
import select 
import sys 
import _thread

class Room:
    def __init__(self, name):
        self.name = name
        self.list_of_clients = [] 

    def clientthread(self, conn, message): 
        # sends a message to the client whose user object is conn 
        conn.send(message.encode()) 
    
    """Using the below function, we broadcast the message to all 
    clients who's object is not the same as the one sending 
    the message """
    def broadcast(self, message, connection): 
        print(message)
        for clients in self.list_of_clients: 
            if clients!=connection: 
                try: 
                    clients.send(message.encode()) 
                except: 
                    clients.close() 
    
                    # if the link is broken, we remove the client 
                    self.remove(clients) 
    
    """The following function simply removes the object 
    from the list that was created at the beginning of 
    the program"""
    def remove(self, connection): 
        if connection in self.list_of_clients: 
            self.list_of_clients.remove(connection) 
    
    def add(self, connection): 
        if connection not in self.list_of_clients: 
            self.list_of_clients.append(connection) 
        _thread.start_new_thread(self.clientthread, (connection, "Welcome to this chatroom!\n\n"))    