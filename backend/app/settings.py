from pydantic_settings import BaseSettings


class CoreSettings(BaseSettings):
    DEBUG: bool = False
    SENTRY_DNS: str


class BetterStackSettings(BaseSettings):
    BS_TOKEN: str
    BS_ID: str
    BS_HOST: str


class Settings(
    CoreSettings,
    BetterStackSettings
):
    pass


settings = Settings()
