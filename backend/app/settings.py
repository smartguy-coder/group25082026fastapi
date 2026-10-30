from pydantic_settings import BaseSettings


class CoreSettings(BaseSettings):
    DEBUG: bool = False
    SENTRY_DNS: str


class BetterStackSettings(BaseSettings):
    BS_TOKEN: str
    BS_ID: str
    BS_HOST: str


class PostgreSQLSettings(BaseSettings):
    POSTGRES_PORT: int = 5432
    POSTGRES_HOST: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


class Settings(
    CoreSettings,
    BetterStackSettings,
    PostgreSQLSettings,
):
    pass


settings = Settings()
