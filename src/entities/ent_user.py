from socket import *
from util.Colors import Colors
import random

__all__ = ['User']


class User:
    def __init__(self, name: str, nick: str, password: str, connection_socket: socket = None):
        self.name: str = name
        self.nickname: str = nick
        self.password: str = password
        self.connection_socket: socket = connection_socket
        self.status_room: str = 'lobby'
        self.is_logged: bool = False
        self.color: Colors = random.choice(Colors.user_colors)

    def toggle_log(self):
        self.is_logged = not self.is_logged

    def set_socket(self, connection_socket: socket):
        self.connection_socket = connection_socket

    def __str__(self):
        return (
                "{" +
                "\n name: " + str(self.name) +
                "\n nick: " + str(self.nickname) +
                "\n password: " + str(self.password) +
                "\n connectionSkt: " + str(self.connection_socket) +
                "\n statusRoom: " + str(self.status_room) +
                "\n isLogged: " + str(self.is_logged) +
                "\n"
                "}"
        )
