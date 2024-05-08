from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    port: int = 8000
    debug: bool = False
    database_url: PostgresDsn
    secret_key: str


settings = Settings()

TORTOISE_CONFIG = {
    'connections': {'default': str(settings.database_url)},
    'apps': {
        'models': {
            'models': ['src.models', 'aerich.models'],
            'default_connection': 'default',
        },
    },
}
