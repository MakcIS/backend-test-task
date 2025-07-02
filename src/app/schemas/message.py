from pydantic import BaseModel
from typing import Literal

class Message(BaseModel):
    message_id: str
    chat_id: str
    text: str
    message_sender: Literal["customer", "employee"]