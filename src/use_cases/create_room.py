import sys
from dtos import dto_room as dtr
from entities import *
from util.PrettyPrint import PrettyPrint
from util.Colors import Colors

__all__ = ['CreateRoom']


class CreateRoom:
    @staticmethod
    def response(user, server, name, max_user) -> None:
        try:
            if name == '' or max_user == '':
                raise Exception("Invalid command")
            room = Room(name, int(max_user))
            server.room_repository.put(dtr.Room(room_id=room.id, name=name, max_participants=max_user))
            server.registered_rooms.append(room)
            user.connection_socket.send(
                (PrettyPrint.pretty_print("Room '" + str(name) + "' created!\n\n", Colors.OKGREEN)).encode())

        except Exception as exp:
            user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in create room '" + str(name) + "' \n\n", Colors.FAIL)).encode())
            tb = sys.exc_info()[2]
            print(exp.with_traceback(tb))
            print()