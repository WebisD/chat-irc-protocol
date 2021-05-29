from socket import socket
from entities import *

__all__ = ['UserFactory']


class UserFactory:
    @staticmethod
    def create(name: str = "FactoredName", nickname: str = "FactoredNickname", password: str = "FactoredPassword",
               connection_socket: socket = None):
        return User(name, nickname, password, connection_socket)
