import time
from threading import Thread
from functions.Help import Help
from functions.Login import Login
from functions.Register import Register
from functions.CreateRoom import CreateRoom
from functions.JoinRoom import JoinRoom
from functions.LeaveRoom import LeaveRoom
from functions.Message import Message

class HandlerRequests(Thread):
    def __init__(self, connectionSocket, server, user):
        Thread.__init__(self)
        self.connectionSocket = connectionSocket
        self.server = server
        self.user = user

    def parseRequest(self, request):
        try:
            print(request)
            request = request.replace('\n', '').replace('\r','')
            print(self.user)
            if self.user.isLogged: 
                if request.find("/create") != -1:
                    CreateRoom.response(self.user, self.server, request.split(' ')[1], request.split(' ')[2])
                elif request.find("/join") != -1:
                    JoinRoom.response(self.user, self.server, request.split(' ')[1])
                elif request.find("/message") != -1:
                    print(request)
                    Message.response(self.user, self.server, request.split(' ')[1])
            else:
                if request.find("/help") != -1:
                    Help.response(self.user)
                elif request.find("/login") != -1:
                    Login.response(self.user, self.server, request.split(' ')[1], request.split(' ')[2])
                elif request.find("/register") != -1:
                    Register.response(self.user, self.server, request.split(' ')[1], request.split(' ')[2],  request.split(' ')[3])
        except:
            self.user.connectionSkt.send( ("Ocorreu um erro ao ler o comando, verifique se você está logado ou se os comandos possuem args corretos\n\n").encode() )
    def run(self):
        while True:
            request = self.connectionSocket.recv(1024).decode()
            
            if not request: 
                break
            else:
                if request.find("/exit") != -1:
                    print("connection closed")
                    self.connectionSocket.close()
                    break
                else:
                    self.parseRequest(request)


