from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Settings(BaseSettings):
    token: SecretStr = None
    
    frequency: int = 10

    db_filename: str = "users.json"

    protect_content: bool = True
    
    model_config = SettingsConfigDict(env_file          = "config.env", 
                                      env_file_encoding = "utf-8")

bot_config = Settings()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
