import asyncio

from tg_photos_to_yadisk_chat_bot.adapters.tg_bot import (
    AllTextMessagesHandler,
    TgBotSettings,
    create_bot,
)


class Settings:
    tg_bot = TgBotSettings()


class Application:
    pass


class TgBotHandlers:
    all_text_messages_handler = AllTextMessagesHandler()


tg_bot = create_bot(
    tg_bot_token=Settings.tg_bot.TG_BOT_TOKEN,
    all_text_messages_handler=TgBotHandlers.all_text_messages_handler,
)

if __name__ == '__main__':
    print('Starting tg bot pooling...')
    asyncio.run(tg_bot.polling())
