import sys
from util import *
from entities.ent_user import *

__all__ = ['Login']


class Login:
    @staticmethod
    def response(user, server, args) -> User:
        try:
            if user.is_logged:
                user.connection_socket.send(
                    (PrettyPrint.pretty_print(
                        "Client '" + str(user.nickname) + "' already logged\n\n", Colors.FAIL
                    )).encode()
                )
                raise Exception("Already logged")

            nickname = args[0]
            password = args[1]

            if nickname == '' or password == '':
                raise Exception("Invalid command")
            nick_ok = False
            pass_ok = False
            logged_ok = False
            user_found: User or None = None

            for userRegistered in server.registered_users:
                if userRegistered.nickname == nickname \
                        and userRegistered.password == password \
                        and not userRegistered.is_logged:

                    user_found = userRegistered
                    nick_ok = True
                    pass_ok = True
                    break

                if userRegistered.nickname == nickname:
                    nick_ok = True
                    if userRegistered.is_logged:
                        logged_ok = True

                if userRegistered.password == password:
                    pass_ok = True

            if nick_ok and pass_ok and not logged_ok:
                user_found.toggle_log()
                user_found.set_socket(user.connection_socket)

                for users in server.active_users:
                    if users.nickname == user.nickname:
                        server.active_users.remove(users)
                        server.active_users.append(user_found)

                user.connection_socket.send(
                    (PrettyPrint.pretty_print("Client " + str(nickname) + " successfully log\n\n",
                                              Colors.OKGREEN)).encode())
                return user_found

            elif logged_ok:
                user.connection_socket.send(
                    (PrettyPrint.pretty_print("Client '" + str(nickname) + "' already logged\n\n", Colors.FAIL)).encode())
            elif not nick_ok:
                user.connection_socket.send(
                    (PrettyPrint.pretty_print("Client '" + str(nickname) + "' not found\n\n", Colors.FAIL)).encode())
            elif not pass_ok:
                user.connection_socket.send(
                    (PrettyPrint.pretty_print("Wrong password\n\n", Colors.FAIL)).encode())

            return user

        except Exception as exp:
            print(exp.with_traceback(sys.exc_info()[2]))
            user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in login client '" + str(args[0]) + "'\n\n", Colors.FAIL)).encode())

            return user
