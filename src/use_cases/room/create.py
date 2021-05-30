import sys
from entities.ent_user import *
from entities.ent_room import *
from util import *

__all__ = ['Create']


class Create:
    @staticmethod
    def response(user, server, args) -> User:
        try:
            if user.status_room != 'lobby':
                user.connection_socket.send(
                 (PrettyPrint.pretty_print("Você já está em uma sala \n\n", Colors.FAIL)).encode())
                return user
            if not user.is_logged:
                user.connection_socket.send(
                 (PrettyPrint.pretty_print("Você deve estar logado \n\n", Colors.FAIL)).encode())
                return user

            name = args[0]
            max_user = args[1]
            room = Room(name, int(max_user))

            for roomRegistered in server.registered_rooms:
                if roomRegistered.name == room.name:
                    user.connection_socket.send(
                        (PrettyPrint.pretty_print("Room '" + str(name) + "' already created!\n\n", Colors.FAIL)).encode())
                    return user
                    
            server.registered_rooms.append(room)
            user.connection_socket.send(
                (PrettyPrint.pretty_print("Room '" + str(name) + "' created!\n\n", Colors.OKGREEN)).encode())

            return user

        except Exception as exp:
            print(exp.with_traceback(sys.exc_info()[2]))
            user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in create room '" + str(args[0]) + "' \n\n", Colors.FAIL)).encode())

            return user
