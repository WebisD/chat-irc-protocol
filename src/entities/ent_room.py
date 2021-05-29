import socket 
import select 
import sys 
import _thread
from typing import List

from entities.ent_user import User
import sys
import os
from util.PrettyPrint import PrettyPrint

__all__ = ['Room']


class Room:
    def __init__(self, name, max_user: int, room_id: str = None):
        self.id = room_id
        self.width = os.get_terminal_size().columns
        self.name: str = name
        self.list_of_clients: List[User] = []
        self.max_user: int = max_user
        self.messages = {
            "user": [],
            "txt": []
        }

    def client_thread(self, user: User, message):
        # sends a message to the client whose user object is conn 
        user.connection_socket.send(message.encode())
    
    """Using the below function, we broadcast the message to all 
    clients who's object is not the same as the one sending 
    the message """
    def broadcast(self, message, user): 
        for client in self.list_of_clients: 
            if client.connection_socket != user.connection_socket:
                try:
                    name_color = PrettyPrint.pretty_print(user.nick, user.color)
                    message_body = (name_color + ": " + message + "\n").rjust(self.width)
                    client.connection_socket.send(message_body.encode())
                    self.messages['user'].append(user.nick)
                    self.messages['txt'].append(message)

                except Exception as exp:
                    client.connection_socket.close()
    
                    # if the link is broken, we remove the client 
                    self.remove(client)

                    tb = sys.exc_info()[2]
                    print(exp.with_traceback(tb))
                    print()
            else:
                user.connection_socket.send(("you said: " + message + "\n").encode())

    def remove(self, user: User) -> bool:
        """
        The following function simply removes the object
        from the list that was created at the beginning of
        the program

        :param user: user that's gonna be removed from the room
        :returns: A boolean representing whether the operation was successful or not
        """
        if user in self.list_of_clients: 
            self.list_of_clients.remove(user) 
            self.broadcast("Sai da sala " + str(user.name), user)
            user.connection_socket.send(("Say goodbye to " + self.name + "!\n\n").encode())
            return True

        return False
    
    def add(self, user: User): 
        if (len(self.list_of_clients) + 1) <= self.max_user:
            if user not in self.list_of_clients: 
                self.list_of_clients.append(user)
            print(self.list_of_clients)
            user.connection_socket.send(("Welcome to " + self.name + "!\n\n").encode())
            self.broadcast("Entrei na sala " + str(user.name), user)
            return True 
        return False
