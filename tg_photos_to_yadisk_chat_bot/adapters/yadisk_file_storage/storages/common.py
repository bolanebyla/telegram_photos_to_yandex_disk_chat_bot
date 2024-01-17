from tg_photos_to_yadisk_chat_bot.application.media_handler.dto import (
    SaveMediaFileStatuses,
    SaveMediaFileToStorageRequestDto,
    SaveMediaFileToStorageResponseDto,
)
from tg_photos_to_yadisk_chat_bot.application.media_handler.interfaces import (
    FileStorage,
)


class YaDiskFileStorage(FileStorage):

    async def save_media(
        self,
        save_media_file_to_storage_request: SaveMediaFileToStorageRequestDto,
    ) -> SaveMediaFileToStorageResponseDto:
        print('File saved')
        return SaveMediaFileToStorageResponseDto(
            status=SaveMediaFileStatuses.SAVED,
        )
