from sqlite3 import *


class DatabaseHandler:
    def __init__(self, dbName: str):
        self.connection: Connection = connect(dbName)
        self.cursor: Cursor = self.connection.cursor()

    def runQuery(self, query: str):
        self.cursor.execute(query)

    def runQueryWithArgs(self, query: str, args: dict):
        self.cursor.execute(query, args)

    def fetchLastQuery(self):
        return self.cursor.fetchone()
