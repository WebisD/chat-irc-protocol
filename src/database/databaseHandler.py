from sqlite3 import *


class DatabaseHandler:
    def __init__(self, dbName: str):
        self.connection: Connection = connect(dbName)
        self.cursor: Cursor = self.connection.cursor()

    def createSchema(self, schemaName: str):
        self.cursor.execute("CREATE SCHEMA :schema_name", {"schema_name": schemaName})
