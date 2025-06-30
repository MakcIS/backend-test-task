from abc import ABC, abstractmethod


class DialogueRepoABC(ABC):
    @abstractmethod
    async def get(self, channel_id: str, chat_id: str):
        pass

    @abstractmethod
    async def create(self, channel_id:str, chat_id:str):
        pass
