from src.core.database.models.dialogue import Dialogue
from core.repositories.mongodb.dialogue import DialogueRepository



class MessageService():

    def __init__(self, repo: DialogueRepository):
        self.repo = repo

    async def get_dialogue_or_create(self, channel_id: str, chat_id:str) -> Dialogue:
        dialogue = await self.repo.get(chat_id=chat_id, channel_id=channel_id)
        if dialogue is None:
            dialogue = await self.repo.create(channel_id=channel_id, chat_id=chat_id)

        return dialogue
