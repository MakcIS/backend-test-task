from src.core.database.models.dialogue import MessageRole


class DialogueMessageEntiti:
    def __init__(self, message_id: str, role: MessageRole, text: str):
        self.message_id = message_id
        self.role = role
        self.text = text

class DialogueEntiti:
    def __init__(self, chat_id:str, channel_id:str, message_list: list,  id:str | None = None):
        self.id = id
        self.chat_id = chat_id
        self.channel_id = channel_id
        self.message_list = message_list

    def add_message(self, message_id: str, role: MessageRole, text: str):
        self.message_list.append(DialogueMessageEntiti(message_id=message_id, role=role, text=text))

