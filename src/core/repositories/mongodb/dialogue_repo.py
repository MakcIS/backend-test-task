from beanie import Document


from core.repositories.interfaces.dialogue import DialogueRepoABC
from src.core.database.models.dialogue import Dialogue

class DialogueRepository(DialogueRepoABC):
    model = Dialogue
        
    async def get(self, channel_id:str, chat_id:str) -> Document | None:
        return await self.model.find_one(self.model.chat_id == chat_id,
                                       self.model.channel_id == channel_id)
    
    async def create(self, channel_id:str, chat_id:str) -> Document:
        dialogue = self.model(chat_id=chat_id,
                              channel_id=channel_id,
                              message_list=[])
        await dialogue.insert()
        return dialogue
        