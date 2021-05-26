import time
from threading import Thread
from useCases.Help import Help
from useCases.Login import Login
from useCases.Register import Register
from useCases.CreateRoom import CreateRoom
from useCases.JoinRoom import JoinRoom
from useCases.LeaveRoom import LeaveRoom
from useCases.Message import Message
from useCases.ListRoom import ListRoom
from useCases.ListUsersRoom import ListUsersRoom


class ControllerRequests(Thread):
    def __init__(self, connectionSocket, server, user):
        Thread.__init__(self)
        self.connectionSocket = connectionSocket
        self.server = server
        self.user = user
        self.commands = ["/create", "/join", "/message", "/help", "/login", "/register"]

    def parseRequest(self, request):
        try:
            request = request.replace('\n', '').replace('\r', '')

            if request.find("/help") != -1:
                Help.response(self.user)
                return

            if self.user.isLogged:
                if request.find("/listusers") != -1:
                    ListUsersRoom.response(self.user, self.server)
                    return

                if request.find("/logout") != -1:
                    if self.user.statusRoom != 'lobby':
                        self.user = LeaveRoom.response(self.user, self.server)
                    self.user.toggleLog()
                    self.user = self.user
                    self.user.connectionSkt.send("Você foi deslogado com sucesso!\n\n".encode())
                    return

                if self.user.statusRoom != 'lobby':
                    if request.find("/message") != -1 or request.find("/m") != -1:
                        Message.response(self.user, self.server, request.replace('/message', '').replace('/m', ''))
                    elif request.find("/leave") != -1:
                        self.user = LeaveRoom.response(self.user, self.server)
                    else:
                        raise Exception("Command invalid")
                else:
                    if request.find("/create") != -1:
                        CreateRoom.response(self.user, self.server, request.split(' ')[1], request.split(' ')[2])
                    elif request.find("/join") != -1:
                        self.user = JoinRoom.response(self.user, self.server, request.split(' ')[1])
                    elif request.find("/listrooms") != -1:
                        ListRoom.response(self.user, self.server)
                    else:
                        raise Exception("Command invalid")

            else:
                if request.find("/login") != -1:
                    self.user = Login.response(self.user, self.server, request.split(' ')[1], request.split(' ')[2])
                elif request.find("/register") != -1:
                    Register.response(self.user, self.server, request.split(' ')[1], request.split(' ')[2],
                                      request.split(' ')[3])
                elif request in self.commands:
                    self.user.connectionSkt.send(("Ocorreu um erro ao ler o comando, verifique se você está logado ou "
                                                  "se os comandos possuem args corretos\n\n").encode())
                else:
                    raise Exception("Command invalid")

        except:
            self.user.connectionSkt.send(("Ocorreu um erro ao ler o comando, verifique se você está logado ou se os "
                                          "comandos possuem args corretos\n\n").encode())

    def run(self):
        while True:
            try:
                request = self.connectionSocket.recv(1024).decode()
                print(self.user.toString())

                if not request:
                    break
                else:
                    if request.find("/exit") != -1:
                        print("connection closed")
                        self.connectionSocket.close()
                        break
                    else:
                        self.parseRequest(request)
            except:
                if self.user.statusRoom != 'lobby':
                    self.user = LeaveRoom.response(self.user, self.server)
                self.connectionSocket.close()
