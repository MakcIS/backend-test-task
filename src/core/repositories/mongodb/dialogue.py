

from src.core.database.models.dialogue import Dialogue, DialogueMessage
from src.core.entities.dialogue import DialogueEntity, DialogueEntity
from src.core.repositories.interfaces.dialogue import DialogueRepoABC


class DialogueRepository(DialogueRepoABC):
    model = Dialogue

    async def get(self, channel_id:str, chat_id:str) -> DialogueEntity | None:
        dialogue =  await self.model.find_one(self.model.chat_id == chat_id,
                                       self.model.channel_id == channel_id)
        if dialogue:
            return DialogueEntity(id=dialogue.id,
                                  chat_id=dialogue.chat_id,
                                  channel_id=dialogue.channel_id,
                                  message_list= [DialogueEntity(message_id=message.message_id, role=message.role, text=message.text) for message in dialogue.message_list],
                                 )
        return None

    async def create(self, chat_id:str, channel_id:str) -> None:
        dialogue = self.model(chat_id=chat_id,
                              channel_id=channel_id,
                              message_list=[])
        await dialogue.insert()
        return DialogueEntity(id=dialogue.id,
                              chat_id=dialogue.chat_id,
                              channel_id=dialogue.channel_id,
                              message_list= [],
                                 )
