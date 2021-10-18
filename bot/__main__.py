import logging

from bot.utils.set_bot_commands import set_default_commands
from bot.data.config import WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT


async def on_startup(dp):
    from . import middlewares
    from bot.loader import bot

    middlewares.setup(dp)

    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)
    await set_default_commands(dp)

if __name__ == '__main__':
    #from aiogram import executor
    from aiogram.utils.executor import start_webhook
    from bot.handlers import dp

    #executor.start_polling(dp, on_startup=on_startup)
    logging.basicConfig(level=logging.INFO)

    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )