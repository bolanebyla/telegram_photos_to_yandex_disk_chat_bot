from telebot.async_telebot import AsyncTeleBot

from .handlers import AllTextMessagesHandler


def create_bot(
    tg_bot_token: str,
    all_text_messages_handler: AllTextMessagesHandler,
) -> AsyncTeleBot:
    bot = AsyncTeleBot(token=tg_bot_token)

    bot.register_message_handler(
        callback=all_text_messages_handler.handle_all_text_messages,
        func=lambda message: True,
        pass_bot=True,
    )

    return bot
