import sys
import difflib
from threading import Thread
from controllers.controller_thread import ControllerThread
from use_cases import *
from controllers import *
from util import *

__all__ = ['ControllerRequests']


class ControllerRequests(Thread):
    """Class of thread responsible for handling incoming requests of the user"""

    def __init__(self, server, incoming_user)  -> None:
        """Initializes the ControllerRequests class instance's attributes

        :param server: Server obj
        :param incoming_user: user obj

        :returns: None
        """
        Thread.__init__(self)
        self.server = server
        self.user = incoming_user

    def parse_request(self, request) -> None:
        """ Responsible for checking the request type and calling the appropriate method

        :param request: A Request object

        :returns: None
        """
        try:
            print(self.user.to_string())
            request = request.replace('\n', '').replace('\r', '').split(' ')

            # Check if it's an abbreviation

            if len(request) <= 0:
                raise Exception("Request length is equal or less than 0")

            if (request[0]).lower() in Help.acronyms.values():
                request[0] = Help.get_full_command((request[0]).lower())

            command = (request[0]).title().replace('/', '')
            print(command)

            args = []
            if len(request) > 1:
                args = request[1:]

            print(command)
            print(args)

            self.user = eval(command).response(self.user, self.server, args)

        except NameError as ne_exp:
            print(ne_exp.with_traceback(sys.exc_info()[2]))

            error_message = "This command does not exist. Type /help to see the commands\n\n"

            logged_commands = Help.logged_commands.keys()
            not_logged_commands = Help.not_logged_commands.keys()

            command = (request[0])

            match = difflib.get_close_matches(command, not_logged_commands) if not self.user.is_logged \
                else difflib.get_close_matches(command, logged_commands)

            if match:
                error_message = f"This command does not exist, did you mean {match[0]}?\n\n"

            self.user.connection_socket.send(
                (PrettyPrint.pretty_print(error_message, Colors.FAIL)).encode())

    def run(self)  -> None:
        """ Responsible for running the thread

        :returns: None
        """
        while True:
            try:
                request = self.user.connection_socket.recv(1024).decode()

                if not request:
                    break
                else:
                    if request.find("/quit") != -1:
                        raise Exception("Close connection")
                    else:
                        self.parse_request(request)

            except Exception as exp:
                print(exp.with_traceback(sys.exc_info()[2]))
                break

        self.close_connection()

    def close_connection(self) -> None:
        """ Responsible for stop the thread and logout user

        :returns: None
        """
        if self.user.status_room != 'lobby':
            self.user = Leave.response(self.user, self.server, [])
        if self.user.is_logged:
            self.user = Logout.response(self.user, self.server, [])

        print("connection closed")
        self.user.connection_socket.send((PrettyPrint.pretty_print("Bye bye!\n\n", Colors.OKGREEN)).encode())
        self.user.connection_socket.close()

        self.server.active_users.remove(self.user)
        ControllerThread.terminate_thread(self)
