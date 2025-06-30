from src.core.database.models.channel import Channel
from src.core.repositories.interfaces.channel import ChannelRepoABC
from src.core.entities.channel_entiti import ChannelEntiti


class ChannelRepository(ChannelRepoABC):
    model = Channel

    async def get(self, bot_name: str) -> ChannelEntiti | None:
        channel =  await self.model.find_one(self.model.chat_bot_name == bot_name)
        if channel:
            return ChannelEntiti(id=channel.id,
                                 chat_bot_name=channel.chat_bot_name,
                                 url=channel.url,
                                 token=channel.token)
        return None

    async def create(self, chat_bot_name:str, url:str, token:str) -> ChannelEntiti:
        channel = self.model(chat_bot_name=chat_bot_name,
                             url=url,
                             token=token)
        await channel.insert()
        return ChannelEntiti(id=channel.id,
                                 chat_bot_name=channel.chat_bot_name,
                                 url=channel.url,
                                 token=channel.token)
    
    