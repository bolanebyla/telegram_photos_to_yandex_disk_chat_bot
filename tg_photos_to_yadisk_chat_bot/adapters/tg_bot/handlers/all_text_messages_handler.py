from attr import dataclass
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message


@dataclass
class AllTextMessagesHandler:

    async def handle_all_text_messages(
        self, message: Message, bot: AsyncTeleBot
    ):
        pass
