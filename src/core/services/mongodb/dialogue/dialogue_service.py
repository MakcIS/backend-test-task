from src.core.database.models.dialogue import Dialogue
from src.core.repositories.mongodb.dialogue_repo import DialogueRepository
from src.core.services.interfaces import dialogue


class DialogueService(dialogue.DialogueServiceABC):

    def __init__(self, repo: DialogueRepository):
        self.repo = repo

    async def get_dialogue_or_create(self, channel_id: str, chat_id:str) -> Dialogue:
        dialogue = await self.repo.get(chat_id=chat_id, channel_id=channel_id)
        if dialogue is None:
            dialogue = await self.repo.create(channel_id=channel_id, chat_id=chat_id)

        return dialogue
