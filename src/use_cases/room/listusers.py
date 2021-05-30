import sys
from util import *

__all__ = ['Listusers']


class Listusers:
    """Class to listusers in the room or the lobby"""

    @staticmethod
    def response(user, server, args) -> None:
        """Performs the listing of users in room or the lobby 
        
        :param server: IP where the server will be allocated 
        :param args: args to list the users 
        
        :returns: user obj with the changes
        """
        try:
            if user.status_room == 'lobby':
                user.connection_socket.send(
                    (PrettyPrint.pretty_print("You are not in a room, my liege \n\n", Colors.FAIL)).encode()
                )

                user.connection_socket.send((
                    "The users in "
                    + PrettyPrint.pretty_print(str("lobby"), Colors.UNDERLINE) + " are the following: \n\n"
                ).encode())

                for users in server.active_users:
                    if users.status_room == "lobby":
                        user.connection_socket.send(
                            (" • " + PrettyPrint.pretty_print(str(users.nickname), Colors.WARNING) + "\n").encode())
                    user.connection_socket.send("\n".encode())
                return user

            for room in server.registered_rooms:
                if room.name == user.status_room:
                    user.connection_socket.send((
                        "The users in room " +
                        PrettyPrint.pretty_print(str(room.name), Colors.UNDERLINE) + " are the following: \n\n"
                    ).encode())

                    for users in room.list_of_clients:
                        user.connection_socket.send(
                            (" • " + PrettyPrint.pretty_print(str(users.nickname), Colors.WARNING) + "\n").encode())
                    user.connection_socket.send("\n".encode())
                    return user

        except Exception as exp:
            print(exp.with_traceback(sys.exc_info()[2]))
            user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in command list \n\n", Colors.FAIL)).encode())
            return user
