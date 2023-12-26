from src.config import TELEGRAM_BOT_TOKEN

from aiogram import Bot
from aiogram.dispatcher import Dispatcher

bot = Bot(TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
