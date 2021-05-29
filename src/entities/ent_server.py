from socket import *
from typing import List
from controllers import *
from entities import *
from repositories import *

__all__ = ['Server', 'start_server']


class Server:
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
        self.socket = server_socket

        self.user_repository: UserRepository = UserRepository()
        self.room_repository: RoomRepository = RoomRepository()
        self.message_repository: MessageRepository = MessageRepository()
        self.participants_repository: ParticipantsRepository = ParticipantsRepository()
        self.room_messages_repository: RoomMessagesRepository = RoomMessagesRepository()
        self.file_repository: FileRepository = FileRepository()
        self.words_repository: WordsRepository = WordsRepository()

        self.controller_connections = ControllerConnections(self)
        self.controller_connections.start()
        self.active_user = []

        registered_rooms, _ = self.room_repository.get_all_rooms()

        if registered_rooms is not None:
            for idx, room in enumerate(registered_rooms):
                registered_rooms[idx] = Room(room.name, room.max_participants, room.id)
        else:
            registered_rooms = []

        self.registered_rooms: List[Room] = registered_rooms

        registered_users, _ = self.user_repository.get_all_users()

        if registered_users is not None:
            for idx, user in enumerate(registered_users):
                registered_users[idx] = User(user.name, user.nickname, user.password)
        else:
            registered_users = []

        self.registered_users: List[User] = registered_users


def start_server() -> None:
    """ It performs the instantiation of an object of type Server, allocating it in the
    local ip and port 8083

    :returns: None
    """
    server_http = Server('localhost', 8083)
    print("Server started on " + server_http.ip + ":" + str(server_http.port))
