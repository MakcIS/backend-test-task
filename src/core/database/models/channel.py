from typing import Annotated
from beanie import Document, Indexed

from src.core.database.models.dialogue import Dialogue

class Channel(Document):
    chat_bot_name: Annotated[str, Indexed(unique=True)] 
    url: str
    token: str