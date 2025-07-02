from abc import ABC, abstractmethod

from src.core.entities.dialogue import DialogueEntity


class DialogueRepoABC(ABC):
    @abstractmethod
    async def get(self, channel_id: str, chat_id: str) -> DialogueEntity:
        pass

    @abstractmethod
    async def create(self, channel_id:str, chat_id:str) -> DialogueEntity:
        pass

    @abstractmethod
    async def update(self, dialogue_entity: DialogueEntity) -> None:
        pass
