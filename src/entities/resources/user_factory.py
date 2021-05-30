from socket import socket
from entities.ent_user import *
from random import randint
from uuid import uuid4
import names

__all__ = ['UserFactory']


class UserFactory:
    @staticmethod
    def create(name: str = None, nickname: str = None, password: str = None,
               connection_socket: socket = None):

        name = names.get_full_name() if name is None else name
        nickname = uuid4().__str__() if nickname is None else nickname
        password = str(randint(0, 10000)) if password is None else password

        return User(name, nickname, password, connection_socket)
