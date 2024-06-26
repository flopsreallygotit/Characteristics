import asyncio, logging, atexit

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from config   import bot_config
from database import db

import handlers

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

async def main():
    logging.basicConfig(level = logging.INFO)

    bot = Bot(token   = bot_config.token.get_secret_value(),
              default = DefaultBotProperties(protect_content = bot_config.protect_content))

    dp = Dispatcher()
    dp.include_routers(handlers.router)

    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    db.save_database()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
