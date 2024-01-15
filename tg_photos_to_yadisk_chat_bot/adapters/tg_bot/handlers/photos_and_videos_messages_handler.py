from attr import dataclass
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, ReactionTypeEmoji

UPLOADED_FILE_REACTION_EMOJI = '💯'


@dataclass
class PhotosAndVideosMessagesHandler:

    async def handle_photos_and_videos(
        self, message: Message, bot: AsyncTeleBot
    ):
        # получаем файл
        photo_size = message.photo[-1]
        photo_info = await bot.get_file(photo_size.file_id)
        photo_bytes = await bot.download_file(photo_info.file_path)
        print(photo_bytes)

        # ставим реакцию, что файл загружен
        await bot.set_message_reaction(
            chat_id=message.chat.id,
            message_id=message.message_id,
            reaction=[ReactionTypeEmoji(emoji=UPLOADED_FILE_REACTION_EMOJI)],
        )
