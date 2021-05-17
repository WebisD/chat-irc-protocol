from socket import *

class User:
    def __init__(self, name, nick, password, connectionSkt):
        self.name = name
        self.nick = nick
        self.password = password
        self.connectionSkt = connectionSkt
        self.statusRoom = 'lobby'
