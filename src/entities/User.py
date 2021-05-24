from socket import *
from Interface.Colors import Colors
import random


class User:
    def __init__(self, name, nick, password, connectionSkt):
        self.name = name
        self.nick = nick
        self.password = password
        self.connectionSkt = connectionSkt
        self.statusRoom = 'lobby'
        self.isLogged = False
        self.color = random.choice(Colors.user_colors)

    def toggleLog(self):
        self.isLogged = not self.isLogged

    def setSocket(self, connectionSkt):
        self.connectionSkt = connectionSkt

    def toString(self):
        return ("{\n" +
        "\n name: " + str(self.name) +
        "\n nick: "+ str(self.nick) +
        "\n password: "+ str(self.password) +
        "\n connectionSkt: "+ str(self.connectionSkt) +
        "\n statusRoom: "+ str(self.statusRoom) +
        "\n isLogged: "+ str(self.isLogged)  +
            "\n}")
            
