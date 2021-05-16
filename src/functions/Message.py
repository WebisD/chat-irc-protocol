class Message:
    @staticmethod
    def response(connectionSocket, server, message) -> None:
        print(message)
        for rooms in server.activeRooms:
            rooms.broadcast(message, connectionSocket)