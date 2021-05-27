from socket import *
from controllers.ControllerConnections import ControllerConnections
from repositories.MessageRepository import MessageRepository
from repositories.ParticipantsRepository import ParticipantsRepository
from repositories.RoomRepository import RoomRepository
from repositories.UserRepository import UserRepository
import src.entities.dtos.User as dto_user
import src.entities.dtos.Room as dto_room
import src.entities.dtos.Message as dto_message


class Server:
    def __init__(self, ip, port):
        """ Performs the creation of an object of type Server, in addition
        will create a handler that will execute on a thread waiting for requests
        :param ip: IP where the server will be allocated
        :param port: Port where the server will be allocated
        """
        self.ip = ip
        self.port = port

        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        serverSocket.bind((self.ip, self.port))
        serverSocket.listen(1)
        self.serverSocket = serverSocket

        self.user_repository: UserRepository = UserRepository()
        self.room_repository: RoomRepository = RoomRepository()
        self.message_repository: MessageRepository = MessageRepository()
        self.participants_repository: ParticipantsRepository = ParticipantsRepository()

        self.controllerConnections = ControllerConnections(self)
        self.controllerConnections.start()    
        self.activeUser = [] 
        self.registeredRooms = [] 
        self.registeredUsers = []


def startServer() -> None:
    """ It performs the instantiation of an object of type Server, allocating it in the
    local ip and port 8083
    """
    serverHttp = Server('localhost', 8083)
    print("Server started on " + serverHttp.ip + ":" + str(serverHttp.port))