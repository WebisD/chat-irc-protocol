import sys
import os
from entities.ent_user import *
from dtos.dto_room import Room as dtoRoom
from util import *
from uuid import uuid4

__all__ = ['Room']


class Room:
    """Class of Room in server"""

    def __init__(self, name, max_user, room_id: str = None) -> None:
        """Initializes the Room class instance's attributes

        :param name: Room's name
        :param max_user: Room's number of maximum users
        :param room_id: Room's id

        :returns: None
        """
        self.id = uuid4().__str__() if room_id is None else room_id
        self.width = os.get_terminal_size().columns
        self.name = name
        self.list_of_clients = []
        self.max_user = max_user
        self.messages = {
            "user": [],
            "txt": []
        }

    def broadcast(self, message, user) -> None:
        """ Send the message to all users in this room (broadcast) 

        :param message:message to be send 
        :param user: user who sent this message 

        :returns: None
        """
        for client in self.list_of_clients:
            if client.connection_socket != user.connection_socket:
                try:
                    name_color = PrettyPrint.pretty_print(user.nickname, user.color)
                    difference = len(name_color) - len(user.nickname)

                    splited_message = PrettyPrint.wrap(user.nickname + message, self.width/2).split('\n')
                    for msg in splited_message:
                        if msg.startswith(user.nickname):
                            message_body = (name_color + ": " + msg[len(user.nickname):] + "\n").rjust(self.width
                                                                                                       + difference)
                        else:
                            message_body = (msg + "\n").rjust(self.width)
                        client.connection_socket.send(message_body.encode())
                    self.messages['user'].append(user.nickname)
                    self.messages['txt'].append(message)

                except Exception as exp:
                    print(exp.with_traceback(sys.exc_info()[2]))
                    client.connection_socket.close()
                    self.remove(client)
            else:
                name_color = PrettyPrint.pretty_print(user.nickname, user.color)
                splited_message = PrettyPrint.wrap(user.nickname + message, self.width / 2).split('\n')

                for msg in splited_message:
                    if msg.startswith(user.nickname):
                        message_body = (name_color + ": " + msg[len(user.nickname):] + "\n")
                    else:
                        message_body = (msg + "\n")
                    client.connection_socket.send(message_body.encode())
                client.connection_socket.send('\n'.encode())

    def remove(self, user: User) -> bool:
        """ Remove an user of room 

        :param user: user who wants to leave room 
        :returns: result of insertion

        """
        if user in self.list_of_clients:
            self.list_of_clients.remove(user)
            self.broadcast(str(user.name) + " left the room", user)
            user.connection_socket.send(("Say goodbye to " + self.name + "!\n\n").encode())
            return True
        return False

    def add(self, user: User) -> bool:
        """ Add a new user in room 

        :param user: user who wants to join 
        :returns: result of insertion

        """
        if (len(self.list_of_clients) + 1) <= self.max_user:
            if user not in self.list_of_clients:
                self.list_of_clients.append(user)
            print(self.list_of_clients)

            user.connection_socket.send(
                (PrettyPrint.pretty_print("Welcome " + self.name + "!\n\n", Colors.OKGREEN)).encode())
            self.broadcast(str(user.name) + " arrived in the room! Say hi 👋", user)
            return True
        return False

    def to_dto(self) -> dtoRoom:
        """ Convert room to dto
        
        :returns: dto obj
        """
        return dtoRoom(name=self.name, max_participants=self.max_user, room_id=self.id)
