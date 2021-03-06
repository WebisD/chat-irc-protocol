import os
import shutil
from threading import Thread
from controllers.controller_requests import *
from entities.resources import *
from util import *

__all__ = ['ControllerConnections']


class ControllerConnections(Thread):
    """Class of thread responsible for handling incoming users"""

    def __init__(self, server) -> None:
        """Initializes the ControllerConnections class instance's attributes

        :param server: server obj

        :returns: None
        """
        Thread.__init__(self)
        self.server = server
        self.width = os.get_terminal_size().columns
        self.terminal_size = shutil.get_terminal_size(fallback=(120, 50))

    def run(self) -> None:
        """ Responsible for running the thread
        
        :returns: None
        """
        while True:
            connection_socket, addr = self.server.server_socket.accept()
            connection_socket.send(('\n' +
                                   (PrettyPrint.pretty_print("CONCORD".center(self.width), Colors.TITLE))).encode())

            connection_socket.send((f"\n\nWelcome to Concord!\n\nDo you want to register or login?\n"
                                   + f"To login run "
                                     f"{PrettyPrint.pretty_print('/login <user> <passw>', Colors.WARNING)} \n"
                                   + f"To register run "
                                     f"{PrettyPrint.pretty_print('/register <name> <user> <passw>', Colors.WARNING)}"
                                     f"\n\n").encode())

            user = UserFactory.create(connection_socket=connection_socket)

            self.server.active_users.append(user)
            handler_requests = ControllerRequests(self.server, user)
            handler_requests.start()
