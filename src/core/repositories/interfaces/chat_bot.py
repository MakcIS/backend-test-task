from abc import ABC, abstractmethod

class ChatBotRepoABC(ABC):
    @abstractmethod
    async def get(self, token:str):
        pass