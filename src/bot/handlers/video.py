import os
import json

from src.loader import dp, bot
from src.config import BASE_PATH

from aiogram import types
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from uuid import uuid4

video_cb = CallbackData("video", "name", "action")


@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def video(message: types.Message):
    if message.caption:
        name = message.caption
    else:
        name = str(uuid4())

    # Download the video
    file = await bot.get_file(message.video.file_id)
    video_data = await bot.download_file(file.file_path)

    # Store the video to your storage (you can customize this part)
    with open(f"{BASE_PATH}/videos/{name}.mp4", "wb") as file:
        file.write(video_data.getvalue())

    await message.answer("Video has been received and stored.")


@dp.message_handler(commands=["videos"])
async def videos(message: types.Message):
    videos = os.listdir(f"{BASE_PATH}/videos")

    if len(videos) <= 1:
        return await message.answer("🛒 There is not video!")

    reply_markup = InlineKeyboardMarkup()

    for video in videos:
        if video == ".gitignore":
            continue

        reply_markup.add(
            InlineKeyboardButton(
                text=video, callback_data=video_cb.new(name=video, action="actions")
            )
        )

    await message.answer(text="🗂 All stored videos", reply_markup=reply_markup)


@dp.callback_query_handler(video_cb.filter(action="actions"))
async def video_show(query: types.CallbackQuery, callback_data: dict):
    await query.answer()

    try:
        await query.message.delete()
    except:
        pass

    await query.message.answer(
        text=f"⚙️ You can select one option.\n\nFile: {callback_data['name']}",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="💫 Add to daily",
                        callback_data=video_cb.new(
                            name=callback_data["name"], action="add-to-daily"
                        ),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="👁 Watch",
                        callback_data=video_cb.new(
                            name=callback_data["name"], action="show"
                        ),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="🗑 Delete",
                        callback_data=video_cb.new(
                            name=callback_data["name"], action="delete"
                        ),
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="❌ Delete only message",
                        callback_data=video_cb.new(
                            name=callback_data["name"], action="remove-message"
                        ),
                    ),
                ],
            ]
        ),
    )


@dp.callback_query_handler(video_cb.filter(action="remove-message"))
async def remove_message(query: types.CallbackQuery):
    await query.answer()

    try:
        await query.message.delete()
    except:
        pass


@dp.callback_query_handler(video_cb.filter(action="show"))
async def show_video(query: types.CallbackQuery, callback_data: dict):
    await query.answer()

    with open(f"{BASE_PATH}/videos/{callback_data['name']}", "rb") as data:
        #
        await query.message.answer_video(video=data, caption=callback_data["name"])


@dp.callback_query_handler(video_cb.filter(action="delete"))
async def delete_video(query: types.CallbackQuery, callback_data: dict):
    try:
        await query.message.delete()
    except:
        pass

    try:
        os.unlink(f"{BASE_PATH}/videos/{callback_data['name']}")

        await query.answer(text="✅ The video is deleted!")
    except:
        await query.answer(text="⚠️ The video can not be deleted!")


@dp.callback_query_handler(video_cb.filter(action="add-to-daily"))
async def add_to_daily(query: types.CallbackQuery, callback_data: dict):
    try:
        await query.message.delete()
    except:
        pass

    try:
        with open(f"{BASE_PATH}/assets/details.json") as file:
            details = json.load(file)
    except FileNotFoundError:
        details = None

    if details:
        details[callback_data["name"]] = {
            "caption": callback_data["name"],
            "counter": 1,
        }
    else:
        details = {
            callback_data["name"]: {
                "caption": callback_data["name"],
                "counter": 1,
            }
        }

    with open(f"{BASE_PATH}/assets/details.json", "w") as file:
        file.write(json.dumps(details, indent=4))

    try:
        os.rename(
            f"{BASE_PATH}/videos/{callback_data['name']}",
            f"{BASE_PATH}/assets/daily/{callback_data['name']}",
        )

        await query.answer(text="✅ The video have been added to list of daily videos!")
    except:
        await query.answer(text="⚠️ The video have not been added to daily videos!")
