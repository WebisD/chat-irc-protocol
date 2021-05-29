from socket import *
from threading import Thread
from entities.ent_user import User
from use_cases.help import Help
from use_cases.login import Login
from use_cases.register import Register
from use_cases.create_room import CreateRoom
from use_cases.join_room import JoinRoom
from use_cases.leave_room import LeaveRoom
from use_cases.message import Message
from use_cases.list_room import ListRoom
from use_cases.list_users_room import ListUsersRoom
from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class ControllerRequests(Thread):
    def __init__(self, connection_socket: socket, server, user: User):
        Thread.__init__(self)
        self.connection_socket: socket = connection_socket
        self.server = server
        self.user: User = user
        self.commands = ["/create", "/join", "/message", "/help", "/login", "/register"]

    def parse_request(self, request):
        try:
            request = request.replace('\n', '').replace('\r', '')

            if request.find("/help") != -1:
                Help.response(self.user)
                return

            if self.user.is_logged:
                if request.find("/listusers") != -1:
                    ListUsersRoom.response(self.user, self.server)
                    return

                if request.find("/logout") != -1:
                    if self.user.status_room != 'lobby':
                        self.user = LeaveRoom.response(self.user, self.server)
                    self.user.toggle_log()
                    self.user = self.user
                    self.user.connection_socket.send(
                        (PrettyPrint.pretty_print("Você foi deslogado com sucesso!\n\n", Colors.OKGREEN)).encode())
                    return

                if self.user.status_room != 'lobby':
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
                        JoinRoom.response(self.user, self.server, request.split(' ')[1])
                    elif request.find("/listrooms") != -1:
                        ListRoom.response(self.user, self.server)
                    else:
                        raise Exception("Command invalid")

            else:
                if request.find("/login") != -1:
                    Login.response(self.user, self.server, request.split(' ')[1], request.split(' ')[2])
                elif request.find("/register") != -1:
                    Register.response(self.user, self.server, request.split(' ')[1], request.split(' ')[2],
                                      request.split(' ')[3])
                elif request in self.commands:
                    self.user.connection_socket.send(
                        (PrettyPrint.pretty_print("Ocorreu um erro ao ler o comando, verifique se você está logado ou "
                                                  "se os comandos possuem args corretos\n\n", Colors.FAIL)).encode())
                else:
                    raise Exception("Command invalid")

        except Exception as exp:
            self.user.connection_socket.send(
                (PrettyPrint.pretty_print("Ocorreu um erro ao ler o comando, verifique se você está logado ou "
                                          "se os comandos possuem args corretos\n\n", Colors.FAIL)).encode())
            print(repr(exp))

    def run(self):
        while True:
            try:
                request = self.connection_socket.recv(1024).decode()
                print(self.user.__str__())

                if not request:
                    break
                else:
                    if request.find("/exit") != -1:
                        print("connection closed")
                        self.connection_socket.close()
                        break
                    else:
                        self.parse_request(request)
            except Exception as exp:
                if self.user.status_room != 'lobby':
                    self.user = LeaveRoom.response(self.user, self.server)
                self.connection_socket.close()
                print(repr(exp))
