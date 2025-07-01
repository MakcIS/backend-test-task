from typing import Literal

from src.core.database.models.dialogue import MessageRole


class DialogueMessageEntity:
    def __init__(self, message_id: str, role: MessageRole, text: str):
        self.message_id = message_id
        self.role = role
        self.text = text

class DialogueEntity:
    def __init__(self, chat_id:str, channel_id:str, message_list: list[DialogueMessageEntity],  id:str | None = None):
        self.id = id
        self.chat_id = chat_id
        self.channel_id = channel_id
        self.message_list = message_list

    def add_message(self, message_id: str, text: str, role: Literal["customer", "employee", None] = None):
        if role == 'customer':
            role = MessageRole.USER
        elif role == 'employee':
            role = MessageRole.SYSTEM
        elif role is None:
            message_id = message_id + "answer"
            role = MessageRole.ASSISTANT
        self.message_list.append(DialogueMessageEntity(message_id=message_id, role=role, text=text))

    def id_list(self):
        return [msg.message_id for msg in self.message_list]
    

