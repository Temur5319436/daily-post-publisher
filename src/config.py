import os

from environs import Env

env = Env()
env.read_env()

BASE_PATH = os.getcwd()

INSTAGRAM_USERNAME = env.str("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = env.str("INSTAGRAM_PASSWORD")

TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
