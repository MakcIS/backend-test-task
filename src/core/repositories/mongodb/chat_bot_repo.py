from beanie import Document

from src.core.repositories.interfaces.chat_bot import ChatBotRepoABC
from src.core.database.models.chat_bot import ChatBot

class ChatBotRepository(ChatBotRepoABC):
    model = ChatBot

    async def get(self, token:str) -> Document | None:
        return await self.model.find_one(self.model.secret_token == token) 