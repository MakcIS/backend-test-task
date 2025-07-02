from abc import ABC, abstractmethod

from src.core.entities.channel import ChannelEntity


class ChannelRepoABC(ABC):
    @abstractmethod
    async def get(self, bot_name: str) -> ChannelEntity:
        pass
