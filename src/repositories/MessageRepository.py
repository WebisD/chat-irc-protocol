from typing import List, Tuple
from repositories.RepositoryInterface import RepositoryInterface
from entities.dtos.Message import Message


class MessageRepository(RepositoryInterface):
    def __init__(self, db_name: str = "concord.db") -> None:
        super().__init__(db_name)
        self.table_name: str = 'room'

    def find_all_by_id(self, message_id: str) -> Tuple[List[Message], bool]:
        try:
            self.database_handler.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where id = :id
                ''',
                {"id": message_id}
            )

            result = self.database_handler.fetch_all_results_from_last_query()
            message_list: List[Message] = []

            for rows in result:
                message_list.append(Message(*rows))

            return message_list, True

        except Exception as exp:
            print(f"Could not find users with id {message_id}")
            print(repr(exp))

        return [], False

    def find_by_id(self, message_id: str) -> Tuple[Message or None, bool]:
        try:
            self.database_handler.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where id = :id
                ''',
                {"id": message_id}
            )

            result = self.database_handler.fetch_one_result_from_last_query()

            if result:
                room = Message(*result)
                return room, True

        except Exception as exp:
            print(f"Could not find room with id {message_id}")
            print(repr(exp))

        return None, False

    def update_by_id(self, message_id: str, new_data: Message) -> bool:
        try:
            self.database_handler.run_query_with_args(
                query=f'''
                    UPDATE {self.table_name}
                    SET 
                        id = :id,
                        name = :name,
                        number_of_participants = :number_of_participants,
                        max_number_of_participants = :max_number_of_participants
                    WHERE id = :userId;
                ''',
                args={"userId": message_id, 
                      "id": new_data.id,
                      "name": new_data.name,
                      "number_of_participants": new_data.num_of_participants,
                      "max_number_of_participants": new_data.max_participants}
            )

            self.database_handler.save_changes()

        except Exception as exp:
            print(f"Could not update room with id {message_id}")
            print(repr(exp))

            return False

        return True

    def delete_by_id(self, message_id: str) -> bool:
        try:
            self.database_handler.run_query_with_args(
                query=f'''
                    DELETE FROM {self.table_name}
                    WHERE id = :id 
                ''',
                args={"id": message_id}
            )

            self.database_handler.save_changes()

        except Exception as exp:
            print(f"Could not delete room with id {message_id}")
            print(repr(exp))

            return False

        return True

    def create(self, room: Message) -> bool:
        try:
            self.database_handler.run_query_with_args(
                query=f'''
                        INSERT INTO {self.table_name}(id,name,number_of_participants,max_number_of_participants) 
                        VALUES (:id,:name,:number_of_participants,:max_number_of_participants)
                ''',
                args={
                    "id": room.id,
                    "name": room.name,
                    "number_of_participants": room.num_of_participants,
                    "max_number_of_participants": room.max_participants
                }
            )

            self.database_handler.save_changes()

        except Exception as exp:
            print(f"Could not create room {room.__str__()}")
            print(repr(exp))

            return False

        return True
