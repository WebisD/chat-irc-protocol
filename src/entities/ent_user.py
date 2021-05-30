from util import *
from dtos.dto_user import User as dtoUser
import random

__all__ = ['User']


class User:
    def __init__(self, name, nickname, password, connection_socket=None):
        self.name = name
        self.nickname = nickname
        self.password = password
        self.connection_socket = connection_socket
        self.status_room = 'lobby'
        self.is_logged = False
        self.color = random.choice(Colors.user_colors)

    def toggle_log(self) -> None:
        self.is_logged = not self.is_logged

    def set_socket(self, connection_socket) -> None:
        self.connection_socket = connection_socket

    def to_string(self) -> str:
        return ("{" +
                "\n name: " + str(self.name) +
                "\n nick: " + str(self.nickname) +
                "\n password: " + str(self.password) +
                "\n connectionSkt: " + str(self.connection_socket) +
                "\n statusRoom: " + str(self.status_room) +
                "\n isLogged: " + str(self.is_logged) +
                "\n}")

    def to_dto(self) -> dtoUser:
        return dtoUser(nickname=self.nickname, name=self.name, password=self.password)
