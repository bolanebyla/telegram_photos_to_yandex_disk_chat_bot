from attr import dataclass
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, ReactionTypeEmoji

from tg_photos_to_yadisk_chat_bot.application.media_handler.dto import (
    SaveMediaFileRequestDto,
    SaveMediaFileStatuses,
)
from tg_photos_to_yadisk_chat_bot.application.media_handler.services import (
    SavingMediaService,
)

UPLOADED_FILE_REACTION_EMOJI = '💯'
UPLOADED_ERROR_REACTION_EMOJI = '🙈'


@dataclass
class PhotosAndVideosMessagesHandler:
    saving_media_service: SavingMediaService

    async def handle_photos_and_videos(
        self, message: Message, bot: AsyncTeleBot
    ):
        # получаем файл
        photo_size = message.photo[-1]
        photo_info = await bot.get_file(photo_size.file_id)
        photo_bytes = await bot.download_file(photo_info.file_path)
        print(photo_bytes)

        save_media_file_response = (
            await self.saving_media_service.save_media_file(
                SaveMediaFileRequestDto(
                    file=photo_bytes,
                    name='test',
                    created_at=message.date,
                )
            )
        )
        if save_media_file_response.status == SaveMediaFileStatuses.SAVED:
            # ставим реакцию, что файл загружен
            await bot.set_message_reaction(
                chat_id=message.chat.id,
                message_id=message.message_id,
                reaction=[
                    ReactionTypeEmoji(emoji=UPLOADED_FILE_REACTION_EMOJI)
                ],
            )
        else:
            await bot.set_message_reaction(
                chat_id=message.chat.id,
                message_id=message.message_id,
                reaction=[
                    ReactionTypeEmoji(emoji=UPLOADED_ERROR_REACTION_EMOJI)
                ],
            )
