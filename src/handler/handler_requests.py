from threading import Thread
from use_cases import *

__all__ = ['HandlerRequests']


class HandlerRequests(Thread):
    def __init__(self, connection_socket, server):
        Thread.__init__(self)
        self.connection_socket = connection_socket
        self.server = server

    def parse_request(self, request):
        print(request)

        request = request.replace('\n', '').replace('\r', '')
        if request.find("/help") != -1:
            Help.response(self.connection_socket)
        elif request.find("/login") != -1:
            Login.response(self.connection_socket, self.server, request.split(' ')[1], request.split(' ')[2])
        elif request.find("/register") != -1:
            Register.response(self.connection_socket, self.server, request.split(' ')[1], request.split(' ')[2], request.split(' ')[3])
        elif request.find("/create") != -1:
            CreateRoom.response(self.connection_socket, self.server, request.split(' ')[1], request.split(' ')[2])
        elif request.find("/join") != -1:
            JoinRoom.response(self.connection_socket, self.server, request.split(' ')[1])
        elif request.find("/message") != -1:
            print(request)
            Message.response(self.connection_socket, self.server, request.split(' ')[1])
        
    def run(self):
        while True:
            request = self.connection_socket.recv(1024).decode()
            print(request)
            if not request: 
                break
            else:
                if request.find("/exit") != -1:
                    # self.server.active_user
                    print("connection closed")
                    self.connection_socket.close()
                    break
                else:
                    self.parse_request(request)


