from enum import StrEnum, auto

from beanie import Document, PydanticObjectId
from pydantic import BaseModel


class MessageRole(StrEnum):
    ASSISTANT = auto()
    SYSTEM = auto()
    USER = auto()


class DialogueMessage(BaseModel):
    role: MessageRole
    text: str


class Dialogue(Document):
    chat_id: str
    channel_id: PydanticObjectId
    is_blocked: bool = False
    message_list: list[DialogueMessage]
