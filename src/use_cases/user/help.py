from entities.ent_user import *
from util import *

__all__ = ['Help']


class Help:
    """Class to show to user all commands"""

    logged_commands = {
        '/help': None,
        '/create': '<room_name> <size>',
        '/listroom': None,
        '/join': '<room_name>',
        '/message': '<your_message>',
        '/listusers': None,
        '/leave': None,
        '/logout': None,
        '/quit': None,
        '/privatemessage': '<receiver_user> <your_message>'
    }
    not_logged_commands = {
        '/help': None,
        '/register': '<name> <pass> <nick>',
        '/login':  '<nick> <pass>',
        '/quit': None,
    }
    acronyms = {
        '/listroom': '/lr',
        '/listusers': '/lu',
        '/message': '/m',
        '/privatemessage': '/pm',
    }

    @staticmethod
    def response(active_user, server, args) -> User:
        """Performs the listing of commands
        
        :param server: IP where the server will be allocated 
        :param args: args to show help commands 
        
        :returns: user obj with the changes
        """
        try:
            message = "\n Available commands"
            list_commands = Help.logged_commands if active_user.is_logged else Help.not_logged_commands

            for _command, _args in list_commands.items():
                full_command = _command + ' ' + _args if _args else _command
                message += f"\n → {PrettyPrint.pretty_print(full_command, Colors.WARNING)}"
                if _command in Help.acronyms:
                    full_command = Help.acronyms[_command] + ' ' + _args if _args else Help.acronyms[_command]
                    message += f" | {PrettyPrint.pretty_print(full_command, Colors.WARNING)}"

            message += '\n\n'

            active_user.connection_socket.send(message.encode())
            return active_user

        except Exception as e:
            print(e)
            active_user.connection_socket.send(
                (PrettyPrint.pretty_print("Error in command help \n\n", Colors.FAIL)).encode())
            return active_user

    @staticmethod
    def get_full_command(value) -> str:
        """Performs the comparision of command
        
        :param value: commands
        
        :returns: command
        """
        for command, abv in Help.acronyms.items():
            if abv == value:
                return command
