import os
import shutil
from threading import Thread
from controllers.controller_requests import *
from entities.ent_user import *
from util import *
from random import randint

__all__ = ['ControllerConnections']


class ControllerConnections(Thread):
    def __init__(self, server):
        Thread.__init__(self)
        self.server = server
        self.width = os.get_terminal_size().columns
        self.terminal_size = shutil.get_terminal_size(fallback=(120, 50))

    def run(self):
        while True:
            connection_socket, addr = self.server.server_socket.accept()
            connection_socket.send(('\n' +
                                   (PrettyPrint.pretty_print("CONCORD".center(self.width), Colors.TITLE))).encode())

            connection_socket.send((f"\n\nSeja bem vindo ao concord!\n\nDeseja se registrar ou logar?\n"
                                   + f"Para logar execute "
                                     f"{PrettyPrint.pretty_print('/login <user> <passw>', Colors.WARNING)} \n"
                                   + f"Para registrar execute "
                                     f"{PrettyPrint.pretty_print('/register <name> <user> <passw>', Colors.WARNING)}"
                                     f"\n\n").encode())

            user = User("UserRandom", "random" + str(randint(0, 10000)), "", connection_socket)

            self.server.active_users.append(user)
            handler_requests = ControllerRequests(self.server, user)
            handler_requests.start()
