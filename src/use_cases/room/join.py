from util import *

__all__ = ['Join']


class Join:
    @staticmethod
    def response(user, server, args) -> None:
        if user.status_room != 'lobby':
            user.connection_socket.send(
                (PrettyPrint.pretty_print("Você já está em uma sala \n\n", Colors.FAIL)).encode())
            return user

        if not user.is_logged:
            user.connection_socket.send(
                (PrettyPrint.pretty_print("Você não está logado amigo \n\n", Colors.FAIL)).encode())
            return user

        room_name = args[0]

        for room in server.registered_rooms:
            if room.name == room_name:
                if room.add(user):
                    user.status_room = room_name
                    return user
        user.connection_socket.send(
            (PrettyPrint.pretty_print("Error in join to room '" + str(room_name) + "' \n\n", Colors.FAIL)).encode())

        return user
