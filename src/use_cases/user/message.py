import sys
from entities.ent_user import *
from util import *

__all__ = ['Message']


class Message:
    @staticmethod
    def response(user, server, args) -> User:
        try:
            if not user.is_logged or user.status_room == 'lobby':
                raise Exception("Invalid command")

            message = " ".join(args)

            for room in server.registered_rooms:
                if room.name == user.status_room:
                    room.broadcast(message, user)
                    return user

        except Exception as exp:
            print(exp.with_traceback(sys.exc_info()[2]))

            message = " ".join(args)

            user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in send message '" + message + "'. Are you logged?' \n\n",
                                          Colors.FAIL)).encode())

        return user
