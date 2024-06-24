from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

from aiogram.enums import ParseMode

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Settings(BaseSettings):
    bot_token: SecretStr = None

    positions: list[str] = ["Я учитель", "Я студент"]

    db_filename: str = "users.json"

    parse_mode: ParseMode = ParseMode.MARKDOWN
    protect_content: bool = True
    
    model_config = SettingsConfigDict(env_file          = "config.env", 
                                      env_file_encoding = "utf-8")

bot_config = Settings()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
