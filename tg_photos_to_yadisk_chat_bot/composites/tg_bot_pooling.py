import asyncio

from tg_photos_to_yadisk_chat_bot.adapters.tg_bot import (
    PhotosAndVideosMessagesHandler,
    TgBotSettings,
    create_bot,
)
from tg_photos_to_yadisk_chat_bot.adapters.yadisk_file_storage import (
    YaDiskFileStorage,
)
from tg_photos_to_yadisk_chat_bot.application.media_handler.services import (
    SavingMediaService,
)


class Settings:
    tg_bot = TgBotSettings()


class Storages:
    ya_disk_file_storage = YaDiskFileStorage()


class Application:
    saving_media_service = SavingMediaService(
        file_storage=Storages.ya_disk_file_storage,
    )


class TgBotHandlers:
    all_text_messages_handler = PhotosAndVideosMessagesHandler(
        saving_media_service=Application.saving_media_service,
    )


tg_bot = create_bot(
    tg_bot_token=Settings.tg_bot.TG_BOT_TOKEN,
    photos_and_videos_messages_handler=TgBotHandlers.all_text_messages_handler,
)

if __name__ == '__main__':
    print('Starting tg bot pooling...')
    asyncio.run(tg_bot.polling())
