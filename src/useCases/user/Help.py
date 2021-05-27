from util.PrettyPrint import PrettyPrint
from util.Colors import Colors


class Help:
    logged_commands = {
        '/help': None,
        '/create': '-room_name -size',
        '/listroom': None,
        '/join': '-room_name',
        '/message': None,
        '/listusers': None,
        '/leave': None,
        '/logout': None,
        '/quit': None,
    }
    not_logged_commands = {
        '/help': None,
        '/register': '-name -pass -nick',
        '/login':  '-nick -pass',
        '/quit': None,
    }

    @staticmethod
    def response(activeUser, server, args) -> None:
        try:
            message = "\n Available commands"
            list_commands = {}

            if activeUser.isLogged:
                list_commands = Help.logged_commands
            else:
                list_commands = Help.not_logged_commands

            for _command, _args in list_commands.items():
                full_command = _command + ' ' + _args if _args else _command
                message += f"\n → {PrettyPrint.pretty_print(full_command, Colors.WARNING)}"

            message += '\n\n'

            activeUser.connectionSkt.send(message.encode())
            return activeUser
        except Exception as e:
            print(e)
            activeUser.connectionSkt.send(
                (PrettyPrint.pretty_print("Error in command help \n\n", Colors.FAIL)).encode())
            return activeUser
