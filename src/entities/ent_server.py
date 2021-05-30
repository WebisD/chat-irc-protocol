from socket import *
from controllers import *

__all__ = ['Server', 'start_server']


class Server:
    def __init__(self, ip, port):
        """ Performs the creation of an object of type Server, in addition
        will create a handler that will execute on a thread waiting for requests
        :param ip: IP where the server will be allocated
        :param port: Port where the server will be allocated
        """
        self.ip = ip
        self.port = port

        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        server_socket.bind((self.ip, self.port))
        server_socket.listen(1)
        self.server_socket = server_socket

        self.controller_connections = ControllerConnections(self)
        self.controller_connections.start()

        self.active_users = []
        self.registered_rooms = []
        self.registered_users = []


def start_server() -> None:
    """ It performs the instantiation of an object of type Server, allocating it in the
    local ip and port 8083
    """
    server_http = Server('localhost', 8083)
    print("Server started on " + server_http.ip + ":" + str(server_http.port))
