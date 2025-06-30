from src.core.database.models.channel import Channel
from src.core.repositories.interfaces.channel import ChannelRepoABC

class ChannelRepository(ChannelRepoABC):
    model = Channel

    async def get(self, bot_name: str) -> Channel | None:
        return await self.model.find_one(self.model.chat_bot_name == bot_name)