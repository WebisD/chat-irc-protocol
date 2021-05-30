import sys
from entities.ent_user import *
from entities.ent_room import *
from entities.ent_server import *
from util import *

__all__ = ['Create']


class Create:
    """Class to create room in server"""

    @staticmethod
    def response(user: User, server, args: list) -> User:
        """Performs the creation of a room in the Server 
        
        :param server: IP where the server will be allocated 
        :param args: args to create the room 
        
        :returns: user obj with the changes
        """
        try:
            if user.status_room != 'lobby':
                user.connection_socket.send(
                 (PrettyPrint.pretty_print("You are already in a room, chief \n\n", Colors.FAIL)).encode())
                return user
            if not user.is_logged:
                user.connection_socket.send(
                 (PrettyPrint.pretty_print("You must login first, buddy \n\n", Colors.FAIL)).encode())
                return user

            name = args[0]
            max_user = args[1]
            room = Room(name, int(max_user))

            for registered_room in server.registered_rooms:
                if registered_room.name == room.name:
                    user.connection_socket.send(
                        (PrettyPrint.pretty_print(
                            "Room '" + str(name) + "' already created!\n\n", Colors.FAIL
                        )).encode())

                    return user
                    
            server.registered_rooms.append(room)
            server.room_repository.put(room.to_dto())

            user.connection_socket.send(
                (PrettyPrint.pretty_print("Room '" + str(name) + "' created!\n\n", Colors.OKGREEN)).encode())

            return user

        except Exception as exp:
            print(exp.with_traceback(sys.exc_info()[2]))
            user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in creating room '" + str(args[0]) + "' \n\n", Colors.FAIL)).encode())

            return user
