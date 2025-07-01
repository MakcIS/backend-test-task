from src.core.database.models.chat_bot import ChatBot
from src.core.repositories.interfaces.chat_bot import ChatBotRepoABC
from src.core.entities.chat_bot import ChatBotEntity


class ChatBotRepository(ChatBotRepoABC):
    model = ChatBot

    async def get(self, token:str) -> ChatBotEntity | None:
        bot =  await self.model.find_one(self.model.secret_token == token)
        if bot:
            return ChatBotEntity(bot_name=bot.name, secret_token=bot.secret_token)
        return None
    
    async def create(self, bot_entiti: ChatBotEntity) -> ChatBotEntity:
        bot = self.model(name=bot_entiti.bot_name, secret_token=bot_entiti.secret_token)
        await bot.insert()
        return ChatBotEntity(bot_name=bot.name, secret_token=bot.secret_token)
