from typing import Annotated
from beanie import Document, Indexed


class ChatBot(Document):
    name: Annotated[str, Indexed(unique=True)]
    secret_token: Annotated[str, Indexed(unique=True)]
