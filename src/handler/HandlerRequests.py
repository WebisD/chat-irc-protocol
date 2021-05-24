import time
from threading import Thread
from commands.Help import Help
from commands.Login import Login
from commands.Register import Register
from commands.CreateRoom import CreateRoom
from commands.JoinRoom import JoinRoom
from commands.LeaveRoom import LeaveRoom
from commands.Message import Message


class HandlerRequests(Thread):
    def __init__(self, connectionSocket, server):
        Thread.__init__(self)
        self.connectionSocket = connectionSocket
        self.server = server

    def parseRequest(self, request):
        print(request)
        request = request.replace('\n', '').replace('\r','')
        if request.find("/help") != -1:
            Help.response(self.connectionSocket, self.server)
        elif request.find("/login") != -1:
            Login.response(self.connectionSocket, self.server, request.split(' ')[1], request.split(' ')[2])
        elif request.find("/register") != -1:
            Register.response(self.connectionSocket, self.server, request.split(' ')[1], request.split(' ')[2],  request.split(' ')[3])
        elif request.find("/create") != -1:
            CreateRoom.response(self.connectionSocket, self.server, request.split(' ')[1], request.split(' ')[2])
        elif request.find("/join") != -1:
            JoinRoom.response(self.connectionSocket, self.server, request.split(' ')[1])
        elif request.find("/message") != -1:
            print(request)
            Message.response(self.connectionSocket, self.server, request.split(' ')[1])
        
    def run(self):
        while True:
            request = self.connectionSocket.recv(1024).decode()
            print(request)
            if not request: 
                break
            else:
                if request.find("/exit") != -1:
                    print("connection closed")
                    self.connectionSocket.close()
                    break
                else:
                    self.parseRequest(request)


