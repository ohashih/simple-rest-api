from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv(verbose=True)


class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()
