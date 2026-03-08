from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_user: str = "tibber"
    db_password: str = "password"
    db_host: str = "localhost"
    db_port: str = "5432"
    db_name: str = "tibber_db"

    class Config:
        env_file = ".env"


settings = Settings()
