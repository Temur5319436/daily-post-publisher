from src.loader import dp

from aiogram import types


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(f"HI !\n\nWhat up {message.from_user.full_name} ?")
