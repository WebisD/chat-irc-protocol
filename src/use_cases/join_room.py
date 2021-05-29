import sys

from util.PrettyPrint import PrettyPrint
from util.Colors import Colors

__all__ = ['JoinRoom']


class JoinRoom:
    @staticmethod
    def response(user, server, room_name) -> None:
        try:
            if room_name == '':
                raise Exception("Invalid command")
            for room in server.registered_rooms:
                if room.name == room_name:
                    if room.add(user):
                        user.status_room = room_name
                        return user
            user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in join to room '" + str(room_name) + "' \n\n", Colors.FAIL)).encode())

        except Exception as exp:
            print("Error in join client")
            tb = sys.exc_info()[2]
            print(exp.with_traceback(tb))
