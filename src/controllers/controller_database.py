import fnmatch
import os
import sys
from sqlite3 import *
from typing import List, Any

__all__ = ['ControllerDatabase']


class ControllerDatabase:
    init: bool = False

    def __init__(self,
                 db_name: str,
                 sql_file_name: str = f"data_model_table_create.sql"
                 ):
        self.connection: Connection = connect(db_name, check_same_thread=False, timeout=5)
        self.cursor: Cursor = self.connection.cursor()

        try:
            sql_file_path = find(sql_file_name, '../')
            with open(sql_file_path[0], 'r', encoding="utf-8") as file:
                if not file:
                    print(f"")
                    raise FileNotFoundError(f"Could not find {sql_file_path}")

                sql_script: str = "".join(file.readlines())

                connection: Connection = connect(db_name)
                connection.cursor().executescript(
                    sql_script
                )
        except Exception as exp:
            tb = sys.exc_info()[2]
            print(exp.with_traceback(tb))
            print()

    @staticmethod
    def initialize(db_name: str, sql_file_path: str) -> bool:
        if ControllerDatabase.init:
            print(f"Database '{db_name}' already initialized")
            return False

        with open(sql_file_path, 'r', encoding="utf-8") as file:
            if not file:
                print(f"")
                return False

            sql_script: str = "".join(file.readlines())

            connection: Connection = connect(db_name)
            connection.cursor().execute(
                sql_script
            )

            ControllerDatabase.init = True

            return True

    def run_query(self, query: str):
        self.cursor.execute(query)

    def run_query_with_args(self, query: str, args: dict):
        self.connection.cursor().execute(query, args)

    def fetch_all_results_from_last_query(self) -> List[Any]:
        return self.cursor.fetchall()

    def fetch_one_result_from_last_query(self) -> Any:
        return self.cursor.fetchone()

    def fetch_some_results_from_last_query(self, number_of_queries: int = 5) -> List[Any]:
        return self.cursor.fetchmany(number_of_queries)

    def save_changes(self):
        self.connection.commit()

    def __del__(self):
        self.connection.close()


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result
