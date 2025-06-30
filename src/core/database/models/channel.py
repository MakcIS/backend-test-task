from typing import Annotated

from beanie import Document, Indexed


class Channel(Document):
    chat_bot_name: Annotated[str, Indexed(unique=True)]
    url: str
    token: str
