from abc import ABC, abstractmethod

from tg_photos_to_yadisk_chat_bot.application.media_handler.dto import (
    SaveMediaFileToStorageRequestDto,
    SaveMediaFileToStorageResponseDto,
)


class FileStorage(ABC):
    """
    Хранилище файлов
    """

    @abstractmethod
    async def save_media(
        self,
        save_media_file_to_storage_request: SaveMediaFileToStorageRequestDto
    ) -> SaveMediaFileToStorageResponseDto:
        """
        Сохраняет файл в хранилище

        :param save_media_file_to_storage_request: - dto для сохранения
        медиа файла в хранилище
        """
        ...
