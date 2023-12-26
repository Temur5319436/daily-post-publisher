import os

from src.loader import dp
from src.config import BASE_PATH

from aiogram import types
from aiogram.utils.callback_data import CallbackData
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

daily_video_cb = CallbackData("daily-video", "name", "action")


@dp.message_handler(commands=["daily"])
async def daily(message: types.Message):
    reply_markup = InlineKeyboardMarkup()

    videos = os.listdir(f"{BASE_PATH}/assets/daily")

    if len(videos) <= 1:
        return await message.answer("🛒 There is not video!")

    for video in videos:
        if video == ".gitignore":
            continue

        reply_markup.add(
            InlineKeyboardButton(
                text=video,
                callback_data=daily_video_cb.new(name=video, action="actions"),
            )
        )

    await message.answer(text=f"📂 List of daily videos!", reply_markup=reply_markup)


@dp.callback_query_handler(daily_video_cb.filter(action="actions"))
async def video_show(query: types.CallbackQuery, callback_data: dict):
    await query.answer()

    try:
        await query.message.delete()
    except:
        pass

    await query.message.answer(
        parse_mode="HTML",
        text=f"⚙️ File: <b>{callback_data['name']}</b>",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="👁 Watch",
                        callback_data=daily_video_cb.new(
                            name=callback_data["name"], action="show"
                        ),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="🗑 Delete",
                        callback_data=daily_video_cb.new(
                            name=callback_data["name"], action="delete"
                        ),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="❌ Delete only message",
                        callback_data=daily_video_cb.new(
                            name=callback_data["name"], action="remove-message"
                        ),
                    ),
                ],
            ]
        ),
    )


@dp.callback_query_handler(daily_video_cb.filter(action="remove-message"))
async def remove_message(query: types.CallbackQuery):
    await query.answer()

    try:
        await query.message.delete()
    except:
        pass


@dp.callback_query_handler(daily_video_cb.filter(action="show"))
async def show_video(query: types.CallbackQuery, callback_data: dict):
    await query.answer()

    with open(f"{BASE_PATH}/assets/daily/{callback_data['name']}", "rb") as data:
        #
        await query.message.answer_video(video=data, caption=callback_data["name"])


@dp.callback_query_handler(daily_video_cb.filter(action="delete"))
async def delete_video(query: types.CallbackQuery, callback_data: dict):
    try:
        await query.message.delete()
    except:
        pass

    try:
        os.unlink(f"{BASE_PATH}/assets/daily/{callback_data['name']}")

        await query.answer(text="✅ The video is deleted!")
    except:
        await query.answer(text="⚠️ The video can not be deleted!")
