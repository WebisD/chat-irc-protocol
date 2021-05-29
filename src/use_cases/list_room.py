from util.PrettyPrint import PrettyPrint
from util.Colors import Colors

__all__ = ['ListRoom']


class ListRoom:
    @staticmethod
    def response(user, server) -> None:
        if user.status_room == 'lobby':
            if len(server.registered_rooms) == 0:
                user.connection_socket.send("There are no rooms here. But you can create one running "
                                            f"{PrettyPrint.pretty_print('/create -room_name -size', Colors.WARNING)} \n\n".encode())
                return

            user.connection_socket.send("The rooms are: \n".encode())
            for room in server.registered_rooms:
                user.connection_socket.send(
                    (" # " + PrettyPrint.pretty_print(str(room.name), Colors.OKCYAN) + "\n").encode())
            user.connection_socket.send('\n'.encode())
            return
        user.connection_socket.send(
            (PrettyPrint.pretty_print("Você já está em uma sala \n\n", Colors.WARNING_BOLD)).encode())
