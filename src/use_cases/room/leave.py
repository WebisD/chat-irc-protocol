import sys
from entities.ent_user import *
from util import *

__all__ = ['Leave']


class Leave:
    @staticmethod
    def response(user, server, args=None) -> User:
        try:
            if not user.is_logged or user.status_room == 'lobby':
                user.connection_socket.send(
                 (PrettyPrint.pretty_print("Você não está em nenhuma sala \n\n", Colors.FAIL)).encode())
                raise Exception("Invalid command")

            for room in server.registered_rooms:
                if room.name == user.status_room:
                    if room.remove(user):
                        user.status_room = 'lobby'
                        user.connection_socket.send(
                            (PrettyPrint.pretty_print("User leave room successfully!\n\n", Colors.OKGREEN)).encode())
                        return user

        except Exception as exp:
            print(exp.with_traceback(sys.exc_info()[2]))
            user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in left room \n\n", Colors.FAIL)).encode())

        return user
