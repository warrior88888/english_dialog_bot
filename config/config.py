from pydantic import Field
from pydantic.types import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


class DatabaseConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="DB_")

    HOST: SecretStr
    PORT: int
    USER: str
    PASS: SecretStr
    NAME: str

    @property
    def url_asyncpg(self):
        # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        return f"postgresql+asyncpg://{self.USER}:{self.PASS.get_secret_value()}@{self.HOST.get_secret_value()}:{self.PORT}/{self.NAME}"


class GptConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="GPT_")

    MODEL: str
    TOKEN: SecretStr


class LogConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="LOG_")

    FORMAT: str
    LEVEL: str


class RedisConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="REDIS_")

    HOST: SecretStr
    PORT: int
    DB: int
    TTL: int


class TelegramConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="TG_")

    TOKEN: SecretStr


class Config(BaseSettings):
    db: DatabaseConfig = Field(default_factory=DatabaseConfig)
    gpt: GptConfig = Field(default_factory=GptConfig)
    log: LogConfig = Field(default_factory=LogConfig)
    redis: RedisConfig = Field(default_factory=RedisConfig)
    telegram: TelegramConfig = Field(default_factory=TelegramConfig)


settings = Config()
