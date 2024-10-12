from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_port: str
    db_user: str
    db_password: str
    db_name: str
    oauth_secret_key: str
    oauth_algorithm: str
    token_expiration_min: int

    class Config:
        env_file = ".env"


settings = Settings()
