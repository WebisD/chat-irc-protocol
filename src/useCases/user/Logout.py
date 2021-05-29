from util.PrettyPrint import PrettyPrint
from util.Colors import Colors
from useCases.room.Leave import Leave
from entities.User import User
from entities.Room import Room
from random import randint


class Logout:
    @staticmethod
    def response(user, server, args) -> None:
        try:
            if not user.isLogged:
                raise Exception("Not logged")

            if user.statusRoom != 'lobby':
                user = Leave.response(user, server)
            user.toggleLog()

            userRandom = User("UserRandom", "random" + str(randint(0, 10000)), "", user.connectionSkt)

            # remove obj with log true and save with log false
            for users in server.registeredUsers:
                if users.nick == user.nick:
                    server.activeUsers.remove(users)
                    server.activeUsers.append(user)

            # the obj in server is random now
            for users in server.activeUsers:
                if users.nick == user.nick:
                    server.activeUsers.remove(users)
                    server.activeUsers.append(userRandom)

            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Você foi deslogado com sucesso!\n\n", Colors.OKGREEN)).encode())
            return userRandom

        except:
            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Error in logout client \n\n", Colors.FAIL)).encode())
            return user
