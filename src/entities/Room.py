import socket 
import select 
import sys 
import _thread
from entities.User import User
import sys
import os
from Interface.PrettyPrint import PrettyPrint
from Interface.Colors import Colors


class Room:
    def __init__(self, name, maxUser):
        self.width = os.get_terminal_size().columns
        self.name = name
        self.list_of_clients = []
        self.maxUser = maxUser
        self.messages = {
            "user": [],
            "txt": []
        }

    def clientthread(self, user, message): 
        # sends a message to the client whose user object is conn 
        user.connectionSkt.send(message.encode()) 
    
    """Using the below function, we broadcast the message to all 
    clients who's object is not the same as the one sending 
    the message """
    def broadcast(self, message, user): 
        for client in self.list_of_clients: 
            if client.connectionSkt != user.connectionSkt:
                try:
                    name_color = PrettyPrint.pretty_print(user.nick, user.color)
                    message_body = (name_color + ": " + message + "\n").rjust(self.width)
                    client.connectionSkt.send(message_body.encode())
                    self.messages['user'].append(user.nick)
                    self.messages['txt'].append(message)

                except: 
                    client.connectionSkt.close() 
    
                    # if the link is broken, we remove the client 
                    self.remove(client) 
            else:
                user.connectionSkt.send(("you said: " + message + "\n").encode())
    
    """The following function simply removes the object 
    from the list that was created at the beginning of 
    the program"""
    def remove(self, user): 
        if user in self.list_of_clients: 
            self.list_of_clients.remove(user) 
            self.broadcast("Sai da sala " + str(user.name), user)
            user.connectionSkt.send(("Say goodbye to " + self.name + "!\n\n").encode())  
            return True
        return False
    
    def add(self, user: User): 
        if (len(self.list_of_clients) + 1) <= self.maxUser:
            if user not in self.list_of_clients: 
                self.list_of_clients.append(user)
            print(self.list_of_clients)
            user.connectionSkt.send(("Welcome to " + self.name + "!\n\n").encode())  
            self.broadcast("Entrei na sala " + str(user.name), user)
            return True 
        return False