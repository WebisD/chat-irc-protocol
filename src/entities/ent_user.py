from util import *
from dtos.dto_user import User as dtoUser
import random

__all__ = ['User']


class User:
    """Class of User in server"""

    def __init__(self, name, nickname, password, connection_socket=None) -> None:
        """Initializes the User class instance's attributes

        :param name: User's name
        :param nickname: User's nickname
        :param password: User's password
        :param connection_socket: User's connection socket

        :returns: None
        """
        self.name = name
        self.nickname = nickname
        self.password = password
        self.connection_socket = connection_socket
        self.status_room = 'lobby'
        self.is_logged = False
        self.color = random.choice(Colors.user_colors)

    def toggle_log(self) -> None:
        """ Invert the status of login 

        :returns: None
        """
        self.is_logged = not self.is_logged

    def set_socket(self, connection_socket) -> None:
        """ Set the user socket 

        :param connectionSkt: socket of user connection 

        :returns: None
        """
        self.connection_socket = connection_socket

    def to_string(self) -> str:
        """ Send the message to all users in this room (broadcast) 

        :param message:message to be send 
        :param user: user who sent this message 

        :returns: None
        """
        return ("{" +
                "\n name: " + str(self.name) +
                "\n nick: " + str(self.nickname) +
                "\n password: " + str(self.password) +
                "\n connectionSkt: " + str(self.connection_socket) +
                "\n statusRoom: " + str(self.status_room) +
                "\n isLogged: " + str(self.is_logged) +
                "\n}")

    def to_dto(self) -> dtoUser:
        """ Convert user to dto
        
        :returns: dto obj
        """
        return dtoUser(nickname=self.nickname, name=self.name, password=self.password)
