from entities.User import User

from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class JoinRoom:
    @staticmethod
    def response(user, server, roomname) -> None:
        try:
            if roomname == '':
                raise Exception("Invalid command")
            for room in server.registeredRooms:
                if room.name == roomname:
                    if room.add(user):
                        user.statusRoom = roomname
                        return user
            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Error in join to room '" + str(roomname) + "' \n\n", Colors.FAIL)).encode())
            return user
        except:
            print("Error in join client")
