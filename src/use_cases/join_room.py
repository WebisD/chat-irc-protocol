import sys
from util.PrettyPrint import PrettyPrint
from util.Colors import Colors
from dtos import dto_participants as dtp

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
                        server.participants_repository.put(dtp.Participants(user.nickname, room_name))

            user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in join to room '" + str(room_name) + "' \n\n", Colors.FAIL)).encode())

        except Exception as exp:
            print("Error in join client")
            tb = sys.exc_info()[2]
            print(exp.with_traceback(tb))
