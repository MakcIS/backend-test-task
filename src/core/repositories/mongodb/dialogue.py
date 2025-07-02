from beanie.odm.operators.update.general import Set

from src.core.database.models.dialogue import Dialogue, DialogueMessage
from src.core.entities.dialogue import DialogueEntity, DialogueMessageEntity
from src.core.repositories.interfaces.dialogue import DialogueRepoABC


class DialogueRepository(DialogueRepoABC):
    model = Dialogue

    async def get(self, channel_id:str, chat_id:str) -> DialogueEntity | None:
        dialogue =  await self.model.find_one(self.model.chat_id == chat_id,
                                       self.model.channel_id == channel_id)
        if dialogue:
            return DialogueEntity(dialogue_id=dialogue.id,
                                  chat_id=dialogue.chat_id,
                                  channel_id=dialogue.channel_id,
                                  message_list= [DialogueMessageEntity(message_id=message.message_id, role=message.role, text=message.text) for message in dialogue.message_list],
                                 )
        return None

    async def create(self, chat_id:str, channel_id:str) -> DialogueEntity:
        dialogue = self.model(chat_id=chat_id,
                              channel_id=channel_id,
                              message_list=[])
        await dialogue.insert()
        return DialogueEntity(dialogue_id=dialogue.id,
                              chat_id=dialogue.chat_id,
                              channel_id=dialogue.channel_id,
                              message_list= [],
                                 )

    async def update(self, dialogue_entity: DialogueEntity) -> None:
        message_list = [DialogueMessage(message_id= msg.message_id,
                                                 role=msg.role,
                                                 text=msg.text) for msg in dialogue_entity.message_list]

        await self.model.find_one(self.model.chat_id == dialogue_entity.chat_id,
                                  self.model.channel_id == dialogue_entity.channel_id).update(Set({"message_list": message_list}))

