from threading import Thread
from useCases.user.Help import Help
from useCases.user.Login import Login
from useCases.user.Logout import Logout
from useCases.user.Register import Register
from useCases.room.Create import Create
from useCases.room.Join import Join
from useCases.room.Leave import Leave
from useCases.user.Message import Message
from useCases.user.Listroom import Listroom
from useCases.room.Listusers import Listusers

from controllers.ControllerThread import ControllerThread

from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class ControllerRequests(Thread):
    def __init__(self, server, user):
        Thread.__init__(self)
        self.server = server
        self.user = user

    def parseRequest(self, request):
        try:
            print(self.user.toString())
            request = request.replace('\n', '').replace('\r', '').split(' ')
            command = (request[0]).title().replace('/', '')
            args = []
            if len(request) > 1:
                args = request[1:]
            print(command)
            print(args)

            self.user = eval(command).response(self.user,self.server, args)
  
        except:
            self.user.connectionSkt.send(
                (PrettyPrint.pretty_print("Ocorreu um erro ao ler o comando, verifique se você está logado ou "
                                          "se os comandos possuem args corretos\n\n", Colors.FAIL)).encode())
            self.user = Help.response(self.user,self.server, [])

    def run(self):
        while True:
            try:
                request = self.user.connectionSkt.recv(1024).decode()

                if not request:
                    break
                else:
                    if request.find("/quit") != -1:
                        raise Exception("Close connection")
                    else:
                        self.parseRequest(request)
            except:
                self.closeConnection()

        

    def closeConnection(self):
        if self.user.statusRoom != 'lobby':
            self.user = LeaveRoom.response(self.user, self.server)

        print("connection closed")
        self.user.connectionSkt.send((PrettyPrint.pretty_print("Bye bye!\n\n", Colors.OKGREEN)).encode())
        self.user.connectionSkt.close()

        self.server.activeUser.remove(self.user)
        ControllerThread.terminate_thread(self)
