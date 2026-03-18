from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "GDG Practice API"
    environment: str = "dev"
    debug: bool = False
    host: str = "127.0.0.1"
    port: int = 8000
    api_key: str = "test-key"   # default de diya

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )

@lru_cache
def get_settings():
    return Settings()
