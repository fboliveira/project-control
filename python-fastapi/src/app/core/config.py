from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    APP_NAME: str
    DATABASE_URL: str

    # Tell Pydantic to read from a .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")