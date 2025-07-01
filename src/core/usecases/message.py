from pydantic import BaseModel
from typing import Literal
from httpx import AsyncClient

from src.predict.mock_llm_call import mock_llm_call
from src.core.repositories.mongodb.chat_bot import ChatBotRepository
from src.core.repositories.mongodb.channel import ChannelRepository
from src.core.repositories.mongodb.dialogue import DialogueRepository

class MessageInput(BaseModel): 
    message_id: str
    chat_id: str
    text: str
    message_sender: Literal["customer", "employee"]

class MessageOutput(BaseModel):
    event_type: Literal["new_message"] = "new_message"
    chat_id: str
    text: str


class MessageUseCase:
    def __init__(self,
                 bot_repo:ChatBotRepository,
                 channel_repo:ChannelRepository,
                 dialogue_repo:DialogueRepository):
        self.bot_repo = bot_repo
        self.channel_repo = channel_repo
        self.dialogue_repo = dialogue_repo

    async def execute(self, token:str, message: MessageInput):
        bot = await self.bot_repo.get(token=token)
        if bot is None:
            pass

        channel = await self.channel_repo.get(bot_name=bot.bot_name)
        if channel is None:
            pass

        dialogue = await self.dialogue_repo.get(channel_id=channel.id, chat_id=message.chat_id)
        
        if dialogue is None:
            dialogue = await self.dialogue_repo.create(chat_id=message.chat_id, channel_id=channel.id)

        if message.message_id in dialogue.id_list():
            pass

        dialogue.add_message(message_id=message.message_id, role=message.message_sender, text=message.text)
        if message.message_sender == 'customer':
            llm_answer = mock_llm_call(chat_history=dialogue.message_list)
            dialogue.add_message(message_id=message.message_id, text=llm_answer, role=None)
            async with AsyncClient() as client:
                await client.post(url=channel.url,
                                  headers={"Authorization": f"Bearer {channel.token}"},
                                  json=MessageOutput(chat_id=message.chat_id,
                                                     text=llm_answer).model_dump())
        self.dialogue_repo.update() #!!!!!!!!!!!!!!!!