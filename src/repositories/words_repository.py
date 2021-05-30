from typing import List, Tuple
from repositories import *
from dtos.dto_words import Words

__all__ = ['WordsRepository']


class WordsRepository(RepositoryInterface):
    def __init__(self, db_name: str = "concord.db") -> None:
        super().__init__(db_name)
        self.table_name: str = 'words'

    def find_all_by_id(self, words_id: str) -> Tuple[List[Words], bool]:
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where id = :words_id
                ''',
                {"words_id": words_id}
            )

            result = self.controller_database.fetch_all_results_from_last_query()
            user_list: List[Words] = []

            for rows in result:
                user_list.append(Words(*rows))

            return user_list, True

        except Exception as exp:
            print(f"Could not find words with id {words_id}")
            print(repr(exp))

        return [], False

    def find_by_id(self, words_id: str) -> Tuple[Words or None, bool]:
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where id = :words_id
                ''',
                {"words_id": words_id}
            )

            result = self.controller_database.fetch_one_result_from_last_query()

            if result:
                user = Words(*result)
                return user, True

        except Exception as exp:
            print(f"Could not find words with id {words_id}")
            print(repr(exp))

        return None, False

    def update_by_id(self, words_id: str, new_data: Words) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    UPDATE {self.table_name}
                    SET id = :words_id, content = :content
                    WHERE id = :search_id;
                ''',
                args={"search_id": words_id, "words_id": new_data.id, "content": new_data.content}
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not update words with id {words_id}")
            print(repr(exp))

            return False

        return True

    def delete_by_id(self, words_id: str) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    DELETE FROM {self.table_name}
                    WHERE id = :words_id 
                ''',
                args={"words_id": words_id}
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not delete words with id {words_id}")
            print(repr(exp))

            return False

        return True

    def put(self, words: Words) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                        INSERT INTO {self.table_name}(id,content) 
                        VALUES (:words_id,:content)
                ''',
                args={"words_id": words.id, "content": words.content}
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not create words {words.__str__()}")
            print(repr(exp))

            return False

        return True
