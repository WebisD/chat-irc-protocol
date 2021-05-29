import sys
import entities as ent
import dtos as dto
from util.PrettyPrint import PrettyPrint
from util.Colors import Colors

__all__ = ['Register']


class Register:
    @staticmethod
    def response(user, server, name: str, nick: str, password: str) -> None:
        try:
            if name == '' or nick == '' or password == '':
                raise Exception("Invalid command")

            user = ent.User(name, nick, password, user.connection_socket)

            for userRegistered in server.registered_users:
                if userRegistered.nick == nick:
                    user.connection_socket.send(
                        (PrettyPrint.pretty_print(
                            "Client '" + str(name) + "' already registered \n\n",
                            Colors.FAIL
                        )).encode()
                    )

                    return None

            server.registered_users.append(user)
            server.user_repository.put(dto.User(user.nick, user.name, user.password))

            user.connection_socket.send(
                (PrettyPrint.pretty_print("Client " + str(name) + " successfully registered \n\n",
                                          Colors.OKGREEN)).encode())

        except Exception as exp:
            user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in register client '" + str(name) + "'\n\n", Colors.FAIL)).encode())
            tb = sys.exc_info()[2]
            print(exp.with_traceback(tb))
