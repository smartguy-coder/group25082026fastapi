from pydantic_settings import BaseSettings


class CoreSettings(BaseSettings):
    DEBUG: bool = False
    BACKEND_HOST: str = 'http://backend:8000'


class Settings(
    CoreSettings,
):
    pass


settings = Settings()
