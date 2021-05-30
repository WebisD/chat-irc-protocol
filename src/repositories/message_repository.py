from typing import List, Tuple
from repositories import *
from dtos.dto_message import Message

__all__ = ['MessageRepository']


class MessageRepository(RepositoryInterface):
    def __init__(self, db_name: str = "concord.db") -> None:
        super().__init__(db_name)
        self.table_name: str = 'message'

    def find_all_by_message_id(self, message_id: str) -> Tuple[List[Message], bool]:
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where id = :id
                ''',
                {"id": message_id}
            )

            result = self.controller_database.fetch_all_results_from_last_query()
            message_list: List[Message] = []

            for rows in result:
                message_list.append(Message(*rows))

            return message_list, True

        except Exception as exp:
            print(f"Could not find messages with id {message_id}")
            print(repr(exp))

        return [], False

    def find_all_by_sender_id(self, sender_id: str) -> Tuple[List[Message], bool]:
        try:
            self.controller_database.run_query_with_args(
                f'''
                        SELECT * from {self.table_name} where sender_id = :id
                    ''',
                {"id": sender_id}
            )

            result = self.controller_database.fetch_all_results_from_last_query()
            message_list: List[Message] = []

            for rows in result:
                message_list.append(Message(*rows))

            return message_list, True

        except Exception as exp:
            print(f"Could not find messages with sender_id {sender_id}")
            print(repr(exp))

        return [], False

    def find_all_by_sender_id_and_receiver_id(self, sender_id: str, receiver_id: str) -> Tuple[List[Message], bool]:
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where sender_id = :sender_id AND receiver_id = :receiver_id
                ''',
                {"sender_id": sender_id, "receiver_id": receiver_id}
            )

            result = self.controller_database.fetch_all_results_from_last_query()
            message_list: List[Message] = []

            for rows in result:
                message_list.append(Message(*rows))

            return message_list, True

        except Exception as exp:
            print(f"Could not find messages with sender_id {sender_id}")
            print(repr(exp))

        return [], False

    def find_all_by_receiver_id(self, receiver_id: str) -> Tuple[List[Message], bool]:
        try:
            self.controller_database.run_query_with_args(
                f'''
                        SELECT * from {self.table_name} where receiver_id = :id
                    ''',
                {"id": receiver_id}
            )

            result = self.controller_database.fetch_all_results_from_last_query()
            message_list: List[Message] = []

            for rows in result:
                message_list.append(Message(*rows))

            return message_list, True

        except Exception as exp:
            print(f"Could not find messages with receiver_id {receiver_id}")
            print(repr(exp))

        return [], False

    def find_by_message_id(self, message_id: str) -> Tuple[Message or None, bool]:
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where id = :id
                ''',
                {"id": message_id}
            )

            result = self.controller_database.fetch_one_result_from_last_query()

            if result:
                message = Message(*result)
                return message, True

        except Exception as exp:
            print(f"Could not find message with id {message_id}")
            print(repr(exp))

        return None, False

    def find_by_sender_id(self, sender_id: str) -> Tuple[Message or None, bool]:
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where sender_id = :id
                ''',
                {"id": sender_id}
            )

            result = self.controller_database.fetch_one_result_from_last_query()

            if result:
                message = Message(*result)
                return message, True

        except Exception as exp:
            print(f"Could not find message with sender_id {sender_id}")
            print(repr(exp))

        return None, False

    def find_by_receiver_id(self, receiver_id: str) -> Tuple[Message or None, bool]:
        try:
            self.controller_database.run_query_with_args(
                f'''
                    SELECT * from {self.table_name} where receiver_id = :id
                ''',
                {"id": receiver_id}
            )

            result = self.controller_database.fetch_one_result_from_last_query()

            if result:
                message = Message(*result)
                return message, True

        except Exception as exp:
            print(f"Could not find message with receiver_id {receiver_id}")
            print(repr(exp))

        return None, False

    def update_by_message_id(self, message_id: str, new_data: Message) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    UPDATE {self.table_name}
                    SET 
                        id = :id,
                        sender_id = :sender_id,
                        receiver_id = :receiver_id,
                        content_id = :content_id,
                        type = :type,
                        date = :date
                    WHERE id = :search_id;
                ''',
                args={
                    "search_id": message_id,
                    "id": new_data.id,
                    "sender_id": new_data.sender_id,
                    "receiver_id": new_data.receiver_id,
                    "content_id": new_data.content_id,
                    "type": new_data.type,
                    "date": new_data.date
                }
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not update message with id {message_id}")
            print(repr(exp))

            return False

        return True

    def update_by_sender_id(self, sender_id: str, new_data: Message) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    UPDATE {self.table_name}
                    SET 
                        id = :id,
                        sender_id = :sender_id,
                        receiver_id = :receiver_id,
                        content_id = :content_id,
                        type = :type,
                        date = :date
                    WHERE sender_id = :search_id;
                ''',
                args={
                    "search_id": sender_id,
                    "id": new_data.id,
                    "sender_id": new_data.sender_id,
                    "receiver_id": new_data.receiver_id,
                    "content_id": new_data.content_id,
                    "type": new_data.type,
                    "date": new_data.date
                }
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not update message with sender_id {sender_id}")
            print(repr(exp))

            return False

        return True

    def update_by_receiver_id(self, receiver_id: str, new_data: Message) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    UPDATE {self.table_name}
                    SET 
                        id = :id,
                        sender_id = :sender_id,
                        receiver_id = :receiver_id,
                        content_id = :content_id,
                        type = :type,
                        date = :date
                    WHERE receiver_id = :search_id;
                ''',
                args={
                    "search_id": receiver_id,
                    "id": new_data.id,
                    "sender_id": new_data.sender_id,
                    "receiver_id": new_data.receiver_id,
                    "content_id": new_data.content_id,
                    "type": new_data.type,
                    "date": new_data.date
                }
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not update message with receiver_id {receiver_id}")
            print(repr(exp))

            return False

        return True

    def delete_by_message_id(self, message_id: str) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    DELETE FROM {self.table_name}
                    WHERE id = :id 
                ''',
                args={"id": message_id}
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not delete message with id {message_id}")
            print(repr(exp))

            return False

        return True

    def delete_by_sender_id(self, sender_id: str) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    DELETE FROM {self.table_name}
                    WHERE sender_id = :id 
                ''',
                args={"id": sender_id}
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not delete message with sender_id {sender_id}")
            print(repr(exp))

            return False

        return True

    def delete_by_receiver_id(self, receiver_id: str) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                    DELETE FROM {self.table_name}
                    WHERE receiver_id = :id 
                ''',
                args={"id": receiver_id}
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not delete message with receiver_id {receiver_id}")
            print(repr(exp))

            return False

        return True

    def put(self, message: Message) -> bool:
        try:
            self.controller_database.run_query_with_args(
                query=f'''
                        INSERT INTO {self.table_name}(id,sender_id,receiver_id,content_id,type,date) 
                        VALUES (:id,:sender_id,:receiver_id,:content_id,:type,:date);
                ''',
                args={
                    "id": message.id,
                    "sender_id": message.sender_id,
                    "receiver_id": message.receiver_id,
                    "content_id": message.content_id,
                    "type": message.type,
                    "date": message.date
                }
            )

            self.controller_database.save_changes()

        except Exception as exp:
            print(f"Could not create message {message.__str__()}")
            print(repr(exp))

            return False

        return True
