from sqlite3 import *


class DatabaseHandler:
    init: bool = False

    def __init__(self,
                 dbName: str,
                 sqlFilePath: str = f"../docs/Relationship Model/DDL Generated/data_model_table_create.sql"):
        self.connection: Connection = connect(dbName)
        self.cursor: Cursor = self.connection.cursor()

        with open(sqlFilePath, 'r', encoding="utf-8") as file:
            if not file:
                print(f"")
                raise FileNotFoundError(f"Could not find {sqlFilePath}")

            sqlScript: str = "".join(file.readlines())

            connection: Connection = connect(dbName)
            connection.cursor().executescript(
                sqlScript
            )

    @staticmethod
    def initialize(dbName: str, sqlFilePath: str) -> bool:
        if DatabaseHandler.init:
            print(f"Database '{dbName}' already initialized")
            return False

        with open(sqlFilePath, 'r', encoding="utf-8") as file:
            if not file:
                print(f"")
                return False

            sqlScript: str = "".join(file.readlines())

            connection: Connection = connect(dbName)
            connection.cursor().execute(
                sqlScript
            )

            DatabaseHandler.init = True

            return True

    def runQuery(self, query: str):
        self.cursor.execute(query)

    def runQueryWithArgs(self, query: str, args: dict):
        self.cursor.execute(query, args)

    def fetchLastQuery(self):
        return self.cursor.fetchall()
