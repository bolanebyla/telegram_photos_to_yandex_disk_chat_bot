from attr import dataclass

from ..dto import (
    SaveMediaFileRequestDto,
    SaveMediaFileResponseDto,
    SaveMediaFileToStorageRequestDto,
)
from ..interfaces import FileStorage

# названия месяцев для создания путей для сохранения файлов
MONTHS_NAMES_MAP_FOR_FILE_PATH = {
    1: '01 январь',
    2: '02 февраль',
    3: '03 март',
    4: '04 апрель',
    5: '05 май',
    6: '06 июнь',
    7: '07 июль',
    8: '08 август',
    9: '09 сентябрь',
    10: '10 октябрь',
    11: '11 ноябрь',
    12: '12 декабрь'
}


@dataclass
class SavingMediaService:
    file_storage: FileStorage

    # TODO: добавить валидацию
    #  @validate_arguments
    async def save_media_file(
        self, save_media_file_request: SaveMediaFileRequestDto
    ) -> SaveMediaFileResponseDto:
        """
        Сохраняет медиа файл в хранилище
        """
        file_path = self._create_file_path_for_file(
            save_media_file_request=save_media_file_request,
        )

        save_media_file_to_storage_response = (
            await self.file_storage.save_media(
                SaveMediaFileToStorageRequestDto(
                    file=save_media_file_request.file,
                    name=save_media_file_request.name,
                    file_path=file_path,
                )
            )
        )

        return SaveMediaFileResponseDto(
            status=save_media_file_to_storage_response.status,
        )

    def _create_file_path_for_file(
        self, save_media_file_request: SaveMediaFileRequestDto
    ) -> str:
        """
        Создает путь по которому нужно сохранить файл
        """
        month_info = MONTHS_NAMES_MAP_FOR_FILE_PATH.get(
            save_media_file_request.created_at.month
        )

        created_year = save_media_file_request.created_at.year

        file_path = f'фото {created_year}/{month_info} {created_year}'
        return file_path
