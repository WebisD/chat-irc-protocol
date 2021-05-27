from util.PrettyPrint import PrettyPrint
from util.Colors import Colors
from useCases.room.Leave import Leave

class Logout:
    @staticmethod
    def response(user, server, args) -> None:
        try:
            if not user.isLogged:
                raise Exception("Not logged")


            if user.statusRoom != 'lobby':
                user = Leave.response(user, server)
            user.toggleLog()
            user = user
            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Você foi deslogado com sucesso!\n\n", Colors.OKGREEN)).encode())
            return user

        except:
            user.connectionSkt.send(
                (PrettyPrint.pretty_print("Error in logout client \n\n", Colors.FAIL)).encode())
            return user
