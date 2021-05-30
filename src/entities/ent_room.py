import sys
import os
from entities.ent_user import *
from util import *

__all__ = ['Room']


class Room:
    def __init__(self, name, max_user):
        self.width = os.get_terminal_size().columns
        self.name = name
        self.list_of_clients = []
        self.max_user = max_user
        self.messages = {
            "user": [],
            "txt": []
        }

    def broadcast(self, message, user):
        for client in self.list_of_clients:
            if client.connection_socket != user.connection_socket:
                try:
                    name_color = PrettyPrint.pretty_print(user.nickname, user.color)
                    message_body = ('\t\t\t\t\t' + name_color + ": " + message + "\n")
                    client.connection_socket.send(message_body.encode())
                    self.messages['user'].append(user.nickname)
                    self.messages['txt'].append(message)

                except Exception as exp:
                    print(exp.with_traceback(sys.exc_info()[2]))
                    client.connection_socket.close()
                    self.remove(client)
            else:
                name_color = PrettyPrint.pretty_print(user.nickname, user.color)
                user.connection_socket.send(('\r\t\t\t\t\t' + name_color + ": " + message + "\n").encode())

    def remove(self, user: User) -> bool:
        if user in self.list_of_clients:
            self.list_of_clients.remove(user)
            self.broadcast("Sai da sala " + str(user.name), user)
            user.connection_socket.send(("Say goodbye to " + self.name + "!\n\n").encode())
            return True
        return False

    def add(self, user: User) -> bool:
        if (len(self.list_of_clients) + 1) <= self.max_user:
            if user not in self.list_of_clients:
                self.list_of_clients.append(user)
            print(self.list_of_clients)

            user.connection_socket.send(
                (PrettyPrint.pretty_print("Welcome " + self.name + "!\n\n", Colors.OKGREEN)).encode())
            self.broadcast("Entrei na sala " + str(user.name), user)
            return True
        return False
