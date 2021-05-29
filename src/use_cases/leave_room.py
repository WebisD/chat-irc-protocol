from entities import *
from util.PrettyPrint import PrettyPrint
from util.Colors import Colors

__all__ = ['LeaveRoom']


class LeaveRoom:
    @staticmethod
    def response(user: User, server) -> User:
        for room in server.registered_rooms:
            if room.name == user.status_room:
                if room.remove(user):
                    user.status_room = 'lobby'

                    return user

            user.connection_socket.send(
                (
                    PrettyPrint.pretty_print(
                        "Error in left room '" + str(room.name) + "'\n\n",
                        Colors.FAIL
                    )
                ).encode()
            )

        return user
