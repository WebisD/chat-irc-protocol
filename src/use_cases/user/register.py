import sys
from entities.ent_user import *
from util import *

__all__ = ['Register']


class Register:
    """Class to register the user in the server"""

    @staticmethod
    def response(user, server, args) -> User:
        """Performs the register of user in the server 
        
        :param server: IP where the server will be allocated 
        :param args: args to register the user 
        
        :returns: user obj with the changes

        """
        try:
            name = args[0]
            nickname = args[1]
            password = args[2]

            if user.is_logged:
                raise Exception("Already logged")

            if name == '' or nickname == '' or password == '':
                raise Exception("Invalid command")

            user_to_register = User(name, nickname, password, user.connection_socket)

            for registered_user in server.registered_users:
                if registered_user.nickname == nickname:
                    user.connection_socket.send(
                        (PrettyPrint.pretty_print(
                            "Client '" + str(name) + "' already registered \n\n", Colors.FAIL
                        )).encode()
                    )

                    return user

            server.registered_users.append(user_to_register)
            server.user_repository.put(user_to_register.to_dto())

            user.connection_socket.send(
                (PrettyPrint.pretty_print(
                    "Client " + str(name) + " successfully registered \n\n", Colors.OKGREEN
                )).encode()
            )

            return user

        except Exception as exp:
            print(exp.with_traceback(sys.exc_info()[2]))

            user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in register client '" + str(args[0]) + "'\n\n", Colors.FAIL)).encode())

        return user
