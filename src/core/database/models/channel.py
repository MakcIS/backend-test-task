from beanie import Document, PydanticObjectId

from src.core.database.models.dialogue import Dialogue

class Channel(Document):
    chat_bot_id: PydanticObjectId
    url: str
    token: str