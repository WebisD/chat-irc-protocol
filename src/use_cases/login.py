import sys
from util.PrettyPrint import PrettyPrint
from util.Colors import Colors

__all__ = ['Login']


class Login:
    @staticmethod
    def response(user, server, nick, password) -> None:
        try:
            if nick == '' or password == '':
                raise Exception("Invalid command")

            nick_ok = False
            pass_ok = False
            logged_ok = False
            user_found = None

            for user_registered in server.registered_users:
                if user_registered.nickname == nick\
                        and user_registered.password == password\
                        and not user_registered.is_logged:
                    user_found = user_registered
                    nick_ok = True
                    pass_ok = True
                    user.nickname = user_registered.nickname
                    user.name = user_registered.name
                    user.password = user_registered.password
                    user.toggle_log()
                    break

                if user_registered.nickname == nick:
                    nick_ok = True
                    if user_registered.is_logged:
                        logged_ok = True
                if user_registered.password == password:
                    pass_ok = True

            if nick_ok and pass_ok and not logged_ok:
                user_found.toggle_log()
                user_found.set_socket(user.connection_socket)
                user.connection_socket.send(
                    (PrettyPrint.pretty_print("Client " + str(nick) + " successfully log\n\n",
                                              Colors.OKGREEN)).encode())
                return user_found
            elif logged_ok:
                user.connection_socket.send(
                    (PrettyPrint.pretty_print("Client '" + str(nick) + "' already logged\n\n", Colors.FAIL)).encode())
            elif not nick_ok:
                user.connection_socket.send(
                    (PrettyPrint.pretty_print("Client '" + str(nick) + "' not found\n\n", Colors.FAIL)).encode())
            elif not pass_ok:
                user.connection_socket.send(
                    (PrettyPrint.pretty_print("Wrong password\n\n", Colors.FAIL)).encode())

        except Exception as exp:
            user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in login client '" + str(nick) + "'\n\n", Colors.FAIL)).encode())
            tb = sys.exc_info()[2]
            print(exp.with_traceback(tb))
