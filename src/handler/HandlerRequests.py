import time
from threading import Thread

class HandlerRequests(Thread):
    def __init__(self, connectionSocket):
        Thread.__init__(self)
        self.connectionSocket = connectionSocket

    @staticmethod
    def parseRequest(request):
        print(request)

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
                    HandlerRequests.parseRequest(request)


