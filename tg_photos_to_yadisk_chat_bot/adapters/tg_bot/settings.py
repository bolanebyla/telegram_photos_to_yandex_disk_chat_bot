from pydantic.v1 import BaseSettings


class TgBotSettings(BaseSettings):
    TG_BOT_TOKEN: str
