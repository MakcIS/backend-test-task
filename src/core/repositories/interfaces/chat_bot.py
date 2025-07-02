from abc import ABC, abstractmethod

from src.core.entities.chat_bot import ChatBotEntity


class ChatBotRepoABC(ABC):
    @abstractmethod
    async def get(self, token:str) -> ChatBotEntity:
        pass
