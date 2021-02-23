import dotenv
from pydantic import BaseSettings

dotenv.load_dotenv('./config/.env')


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    APP_PORT: int
    APP_HOST: str
    APP_ENV: str
    DEBUG: bool
    RELOAD: bool
    PROJECT_NAME: str
    VERSION: str
    DESCRIPTION: str
    BASE_URL: str

    def get_env_settings(self) -> None:
        if self.APP_ENV == "DEVELOPMENT":
            self.RELOAD = True
            self.DEBUG = True

        elif self.APP_ENV == "PRODUCTION":
            self.RELOAD = False
            self.DEBUG = False

    class Config:
        env_file = './config/.env'
        env_file_encoding = 'utf-8'

    def get_db_uri(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
settings.get_env_settings()
