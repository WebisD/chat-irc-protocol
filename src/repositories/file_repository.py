from typing import List, Tuple
from repositories import *
from dtos.dto_file import File

__all__ = ['FileRepository']


class FileRepository(RepositoryInterface):
    def __init__(self, db_name: str = "concord.db") -> None:
        super().__init__(db_name)
        self.table_name: str = 'file'

    def find_all_by_id(self, file_id: str) -> Tuple[List[File], bool]:
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where id = :file_id
                ''',
                {"file_id": file_id}
            )

            result = self.controller_database.fetch_all_results_from_last_query()
            user_list: List[File] = []

            for rows in result:
                user_list.append(File(*rows))

            return user_list, True

        except Exception as exp:
            print(f"Could not find files with id {file_id}")
            print(repr(exp))

        return [], False

    def find_by_id(self, words_id: str) -> Tuple[File or None, bool]:
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where id = :file_id
                ''',
                {"file_id": words_id}
            )

            result = self.controller_database.fetch_one_result_from_last_query()

            if result:
                user = File(*result)
                return user, True

        except Exception as exp:
            print(f"Could not find file with id {words_id}")
            print(repr(exp))

        return None, False

    def update_by_id(self, file_id: str, new_data: File) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    UPDATE {self.table_name}
                    SET id = :file_id, name = :name, content = :content
                    WHERE id = :search_id;
                ''',
                args={"search_id": file_id, "file_id": new_data.id, "name": new_data.name, "content": new_data.content}
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not update file with id {file_id}")
            print(repr(exp))

            return False

        return True

    def delete_by_id(self, file_id: str) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    DELETE FROM {self.table_name}
                    WHERE id = :file_id 
                ''',
                args={"file_id": file_id}
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not delete file with id {file_id}")
            print(repr(exp))

            return False

        return True

    def put(self, file: File) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                        INSERT INTO {self.table_name}(id, name, content) 
                        VALUES (:file_id,:name,:content);
                ''',
                args={"file_id": file.id, "name": file.name, "content": file.content}
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not create file {file.__str__()}")
            print(repr(exp))

            return False

        return True
