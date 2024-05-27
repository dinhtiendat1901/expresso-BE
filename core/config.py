from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://root:123456@localhost:3306/fast_api_db"

    class Config:
        env_file = ".env"


settings = Settings()
