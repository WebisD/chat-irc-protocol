from entities.User import User
from entities.Room import Room

from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class Leave:
    @staticmethod
    def response(user, server, args) -> None:
        try:
            if not user.isLogged or user.statusRoom == 'lobby':
                raise Exception("Invalid command")

            for room in server.registeredRooms:
                if room.name == user.statusRoom:
                    if room.remove(user):
                        user.statusRoom = 'lobby'
                        user.connectionSkt.send(
                            (PrettyPrint.pretty_print("User leave room successfully!\n\n", Colors.OKGREEN)).encode())
                        return user
        except:
            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Error in left room \n\n", Colors.FAIL)).encode())
            return user

        