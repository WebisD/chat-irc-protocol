import sys
from util import *
from entities.ent_user import *

__all__ = ['Listroom']


class Listroom:
    @staticmethod
    def response(user, server, args) -> User:
        try:
            if user.status_room != 'lobby':
                user.connection_socket.send(
                    (PrettyPrint.pretty_print("You are already in a room, my dancing queen \n\n", Colors.FAIL)).encode()
                )

                return user
                
            if len(server.registered_rooms) == 0:
                user.connection_socket.send(
                    "There are no rooms here. But you can create one by running "
                    f"{PrettyPrint.pretty_print('/create -room_name -size', Colors.WARNING)} \n\n".encode()
                )

                return user
    
            user.connection_socket.send("The rooms are the following: \n".encode())

            for room in server.registered_rooms:
                user.connection_socket.send(
                    (" # " + PrettyPrint.pretty_print(str(room.name), Colors.OKCYAN) + "\n").encode()
                )

            user.connection_socket.send('\n'.encode())

            return user

        except Exception as exp:
            print(exp.with_traceback(sys.exc_info()[2]))
            user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in command list \n\n", Colors.FAIL)).encode())
            return user
