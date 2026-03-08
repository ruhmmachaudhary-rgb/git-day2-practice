from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    API_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Create a settings instance
settings = Settings()
