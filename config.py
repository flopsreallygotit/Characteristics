from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Settings(BaseSettings):
    token: SecretStr = None
    
    max_query_count: int = 5

    db_filename: str = "users.json"

    protect_content: bool = False
    
    model_config = SettingsConfigDict(env_file          = "config.env", 
                                      env_file_encoding = "utf-8")

bot_config = Settings()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
