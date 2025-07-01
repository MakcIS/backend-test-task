from asyncio import sleep
from random import randint

from core.entities.dialogue import DialogueMessageEntity


async def mock_llm_call(chat_history: list[DialogueMessageEntity]) -> str:
    await sleep(randint(1, 5))
    return "New message from llm"
