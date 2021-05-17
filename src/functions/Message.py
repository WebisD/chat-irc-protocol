class Message:
    @staticmethod
    def response(connectionSocket, server, message) -> None:
        print(message)
        for rooms in server.activeRooms:
            print(rooms)
            rooms.broadcast(message, connectionSocket)