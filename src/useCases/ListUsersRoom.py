from entities.User import User
from entities.Room import Room

from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class ListUsersRoom:
    @staticmethod
    def response(user, server) -> None:
        for room in server.registeredRooms:
            if room.name == user.statusRoom:
                user.connectionSkt.send(("Os usuários na sala " + PrettyPrint.pretty_print(str(room.name), Colors.UNDERLINE) + "são: \n\n").encode())
                for users in room.list_of_clients:
                    user.connectionSkt.send((" • " + PrettyPrint.pretty_print(str(users.nick), Colors.WARNING) + "\n").encode())
                user.connectionSkt.send("\n".encode())
                return
        user.connectionSkt.send(
            (PrettyPrint.pretty_print("Você não está em nenhuma sala \n\n", Colors.FAIL)).encode())
