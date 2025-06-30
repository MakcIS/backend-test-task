from abc import ABC, abstractmethod

class DialogueServiceABC(ABC):
    @abstractmethod
    async def get_dialogue_or_create(self, channel_id:str, chat_id:str):
        pass
    
    @abstractmethod
    async def check_massage_id(self, channel_id:str, chat_id:str) -> bool:
        pass