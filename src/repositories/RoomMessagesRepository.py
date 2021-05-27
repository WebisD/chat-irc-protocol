from typing import List, Tuple
from repositories.RepositoryInterface import RepositoryInterface
from entities.dtos.RoomMessages import RoomMessages


class RoomMessagesRepository(RepositoryInterface):
    def __init__(self, db_name: str = "concord.db") -> None:
        super().__init__(db_name)
        self.table_name: str = 'room_messages'

    def find_all_by_user_id(self, message_id: str) -> Tuple[List[RoomMessages], bool]:
        try:
            self.database_handler.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where message_id = :id
                ''',
                {"id": message_id}
            )

            result = self.database_handler.fetch_all_results_from_last_query()
            message_list: List[RoomMessages] = []

            for rows in result:
                message_list.append(RoomMessages(*rows))

            return message_list, True

        except Exception as exp:
            print(f"Could not find room_messages with message_id {message_id}")
            print(repr(exp))

        return [], False

    def find_all_by_room_id(self, room_id: str) -> Tuple[List[RoomMessages], bool]:
        try:
            self.database_handler.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where room_id = :id
                ''',
                {"id": room_id}
            )

            result = self.database_handler.fetch_all_results_from_last_query()
            message_list: List[RoomMessages] = []

            for rows in result:
                message_list.append(RoomMessages(*rows))

            return message_list, True

        except Exception as exp:
            print(f"Could not find room_messages with room_id {room_id}")
            print(repr(exp))

        return [], False

    def find_one_by_user_id(self, message_id: str) -> Tuple[RoomMessages or None, bool]:
        try:
            self.database_handler.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where message_id = :id
                ''',
                {"id": message_id}
            )

            result = self.database_handler.fetch_one_result_from_last_query()

            if result:
                message = RoomMessages(*result)
                return message, True

        except Exception as exp:
            print(f"Could not find participant with room_id {message_id}")
            print(repr(exp))

        return None, False

    def find_one_by_room_id(self, room_id: str) -> Tuple[RoomMessages or None, bool]:
        try:
            self.database_handler.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where room_id = :id
                ''',
                {"id": room_id}
            )

            result = self.database_handler.fetch_one_result_from_last_query()

            if result:
                message = RoomMessages(*result)
                return message, True

        except Exception as exp:
            print(f"Could not find room_message with room_id {room_id}")
            print(repr(exp))

        return None, False

    def update_by_user_id(self, message_id: str, new_data: RoomMessages) -> bool:
        try:
            self.database_handler.run_query_with_args(
                query=f'''
                    UPDATE {self.table_name}
                    SET 
                        message_id = :message_id,
                        room_id = :room_id

                    WHERE message_id = :search_user_id;
                ''',
                args={
                    "search_user_id": message_id,
                    "message_id": new_data.message_id,
                    "room_id": new_data.room_id
                }
            )

            self.database_handler.save_changes()

        except Exception as exp:
            print(f"Could not update room_messages with room_id {message_id}")
            print(repr(exp))

            return False

        return True

    def update_by_room_id(self, room_id: str, new_data: RoomMessages) -> bool:
        try:
            self.database_handler.run_query_with_args(
                query=f'''
                    UPDATE {self.table_name}
                    SET 
                        user_id = :message_id,
                        room_id = :room_id

                    WHERE room_id = :search_room_id;
                ''',
                args={
                    "search_room_id": room_id,
                    "message_id": new_data.message_id,
                    "room_id": new_data.room_id
                }
            )

            self.database_handler.save_changes()

        except Exception as exp:
            print(f"Could not update room_messages with room_id {room_id}")
            print(repr(exp))

            return False

        return True

    def delete_by_user_id(self, message_id: str) -> bool:
        try:
            self.database_handler.run_query_with_args(
                query=f'''
                    DELETE FROM {self.table_name}
                    WHERE user_id = :message_id 
                ''',
                args={"message_id": message_id}
            )

            self.database_handler.save_changes()

        except Exception as exp:
            print(f"Could not delete room_messages with message_id {message_id}")
            print(repr(exp))

            return False

        return True

    def delete_by_room_id(self, room_id: str) -> bool:
        try:
            self.database_handler.run_query_with_args(
                query=f'''
                    DELETE FROM {self.table_name}
                    WHERE room_id = :room_id 
                ''',
                args={"room_id": room_id}
            )

            self.database_handler.save_changes()

        except Exception as exp:
            print(f"Could not delete room_messages with room_id {room_id}")
            print(repr(exp))

            return False

        return True

    def create(self, room_messages: RoomMessages) -> bool:
        try:
            self.database_handler.run_query_with_args(
                query=f'''
                        INSERT INTO {self.table_name}(message_id, room_id) 
                        VALUES (:message_id,:room_id);
                ''',
                args={
                    "message_id": room_messages.message_id,
                    "room_id": room_messages.room_id,
                }
            )

            self.database_handler.save_changes()

        except Exception as exp:
            print(f"Could not create room_messages {room_messages.__str__()}")
            print(repr(exp))

            return False

        return True
