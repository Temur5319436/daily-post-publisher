import os

from environs import Env

env = Env()
env.read_env()

ENV = env.str("ENV")

BASE_PATH = os.getcwd()

INSTAGRAM_USERNAME = env.str("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = env.str("INSTAGRAM_PASSWORD")

TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")

WEBHOOK_HOST = env.str("WEBHOOK_HOST")
WEBHOOK_PATH = env.str("WEBHOOK_PATH")

WEBAPP_HOST = env.str("WEBAPP_HOST")
WEBAPP_PORT = env.int("WEBAPP_PORT")
