from aiogram import executor


from src import config
from src.loader import dp, bot


async def on_startup(dp):
    await bot.set_webhook(f"{config.WEBHOOK_HOST}{config.WEBHOOK_PATH}")


def app():
    if config.ENV == "production":
        executor.start_webhook(
            dispatcher=dp,
            webhook_path=config.WEBHOOK_PATH,
            skip_updates=True,
            on_startup=on_startup,
            host=config.WEBAPP_HOST,
            port=config.WEBAPP_PORT,
        )

    else:
        executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    app()
