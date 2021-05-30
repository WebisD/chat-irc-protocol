from socket import *
from typing import List
from controllers import *
from repositories import *
from entities import *

__all__ = ['Server', 'start_server']


class Server:
    """Class of Server"""

    def __init__(self, ip, port) -> None:
        """ Performs the creation of an object of type Server, in addition
        will create a handler that will execute on a thread waiting for requests

        :param ip: IP where the server will be allocated
        :param port: Port where the server will be allocated

        :returns: None
        """
        self.ip = ip
        self.port = port

        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        server_socket.bind((self.ip, self.port))
        server_socket.listen(1)
        self.server_socket = server_socket

        self.user_repository: UserRepository = UserRepository()
        self.room_repository: RoomRepository = RoomRepository()
        self.message_repository: MessageRepository = MessageRepository()
        self.participants_repository: ParticipantsRepository = ParticipantsRepository()
        self.room_messages_repository: RoomMessagesRepository = RoomMessagesRepository()
        self.file_repository: FileRepository = FileRepository()
        self.words_repository: WordsRepository = WordsRepository()

        self.controller_connections = ControllerConnections(self)
        self.controller_connections.start()

        self.active_users = []
        self.registered_rooms: List[ent_room.Room] = self.__get_registered_rooms()
        self.registered_users: List[ent_user.User] = self.__get_registered_users()

    def __get_registered_rooms(self) -> List[ent_room.Room]:
        """ Return the list of registered rooms in the server

        :returns: list of rooms
        """
        registered_rooms: List[ent_room.Room] = []
        rooms, _ = self.room_repository.get_all_rooms()

        if rooms is None:
            return []

        for room in rooms:
            registered_rooms.append(ent_room.Room(room.name, room.max_participants, room.id))

        return registered_rooms

    def __get_registered_users(self) -> List[ent_user.User]:
        """ Return the list of registered users in the server

        :returns: list of users
        """
        registered_users: List[ent_user.User] = []
        users, _ = self.user_repository.get_all_users()

        if users is None:
            return []

        for user in users:
            registered_users.append(ent_user.User(user.name, user.nickname, user.password))

        return registered_users


def start_server() -> None:
    """ It performs the instantiation of an object of type Server, allocating it in the
    local ip and port 8083
    
    :returns: None
    """
    server_http = Server('localhost', 8083)
    print("Server started on " + server_http.ip + ":" + str(server_http.port))
