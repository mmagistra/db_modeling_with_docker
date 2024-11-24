from os import getenv
from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent

DB_PATH = BASE_DIR / "db.sqlite3"

# DB_URL = getenv('DATABASE_URL', f"sqlite+aiosqlite:///{DB_PATH}")
DB_URL = getenv('DATABASE_URL', f"postgresql://"
                                f"{getenv('POSTGRES_USER')}:"
                                f"{getenv('POSTGRES_PASSWORD')}@postgres_container/"
                                f"{getenv('POSTGRES_DB')}")
CURRENT_SETTINGS = getenv('SETTINGS', 'ProdSettings')

print('OUR DB URL IS ', DB_URL)
print('CURRENT SETTINGS IS ', CURRENT_SETTINGS)


class Settings(BaseSettings):
    db_url: str = DB_URL
    echo: bool = False
    # echo: bool = True


class TestSettings(Settings):
    # echo: bool = False
    echo: bool = True


class ProdSettings(Settings):
    echo: bool = False
    # echo: bool = True


settings_dict = {
    'ProdSettings': ProdSettings,
    'TestSettings': TestSettings
}


settings = settings_dict.get(CURRENT_SETTINGS, ProdSettings)()
