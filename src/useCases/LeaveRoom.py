from entities.User import User
from entities.Room import Room

from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class LeaveRoom:
    @staticmethod
    def response(user, server) -> None:
        for room in server.registeredRooms:
            if room.name == user.statusRoom:
                if room.remove(user):
                    user.statusRoom = 'lobby'
                    return user
        user.connectionSkt.send(
            (PrettyPrint.pretty_print("Error in left room '" + str(room.name) + "'\n\n", Colors.FAIL)).encode())
        return user