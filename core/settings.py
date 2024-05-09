from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    admin_id: int
    db_password: str
    Backup_path: str


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(bots=Bots(bot_token=env.str("DEV_TOKEN"), admin_id=env.int("ADMIN_ID"), db_password=env.str("DB_password"), Backup_path=env.str("Backup_path")))


Setting = get_settings('Secret.txt')
