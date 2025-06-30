from abc import ABC, abstractmethod


class ChannelRepoABC(ABC):
    @abstractmethod
    async def get(self, bot_name: str):
        pass
