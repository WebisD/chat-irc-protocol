from entities.User import User

from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class Join:
    @staticmethod
    def response(user, server, args) -> None:
        if user.statusRoom != 'lobby':
            user.connectionSkt.send(
            (PrettyPrint.pretty_print("Você já está em uma sala \n\n", Colors.FAIL)).encode())
            return user

        if not user.isLogged:
            user.connectionSkt.send(
            (PrettyPrint.pretty_print("Você não está logado amigo \n\n", Colors.FAIL)).encode())
            return user

        roomname = args[0]
    
        for room in server.registeredRooms:
            if room.name == roomname:
                if room.add(user):
                    user.statusRoom = roomname
                    return user
        user.connectionSkt.send(
            (PrettyPrint.pretty_print("Error in join to room '" + str(roomname) + "' \n\n", Colors.FAIL)).encode())
        return user
