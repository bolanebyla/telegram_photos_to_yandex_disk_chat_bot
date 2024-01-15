from telebot.async_telebot import AsyncTeleBot

from .handlers import PhotosAndVideosMessagesHandler


def create_bot(
    tg_bot_token: str,
    photos_and_videos_messages_handler: PhotosAndVideosMessagesHandler,
) -> AsyncTeleBot:
    bot = AsyncTeleBot(token=tg_bot_token)

    bot.register_message_handler(
        callback=photos_and_videos_messages_handler.handle_photos_and_videos,
        content_types=['photo', 'video'],
        pass_bot=True,
    )

    return bot
