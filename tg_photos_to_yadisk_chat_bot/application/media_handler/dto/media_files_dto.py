from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class SaveMediaFileRequestDto(BaseModel):
    """
    Запрос на сохранение медиа файла
    """
    file: bytes
    name: str
    created_at: datetime


class SaveMediaFileToStorageRequestDto(BaseModel):
    """
    Запрос на сохранение медиа файла в хранилище
    """
    file: bytes
    name: str
    file_path: str


class SaveMediaFileStatuses(Enum):
    """
    Статусы результата сохранения файла
    """
    SAVED = 1
    ALREADY_EXISTS = 2
    ERROR = 3


class SaveMediaFileToStorageResponseDto(BaseModel):
    """
    Результат сохранения медиа файла в хранилище
    """
    status: SaveMediaFileStatuses


class SaveMediaFileResponseDto(BaseModel):
    """
    Результат сохранения медиа файла
    """
    status: SaveMediaFileStatuses
