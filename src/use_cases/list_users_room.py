from util.PrettyPrint import PrettyPrint
from util.Colors import Colors

__all__ = ['ListUsersRoom']


class ListUsersRoom:
    @staticmethod
    def response(user, server) -> None:
        for room in server.registered_rooms:
            if room.name == user.status_room:
                user.connection_socket.send(("Os usuários na sala " + PrettyPrint.pretty_print(str(room.name), Colors.UNDERLINE) + "são: \n\n").encode())
                for users in room.list_of_clients:
                    user.connection_socket.send((" • " + PrettyPrint.pretty_print(str(users.nickname), Colors.WARNING) + "\n").encode())
                user.connection_socket.send("\n".encode())
                return
        user.connection_socket.send(
            (PrettyPrint.pretty_print("Você não está em nenhuma sala \n\n", Colors.FAIL)).encode())
