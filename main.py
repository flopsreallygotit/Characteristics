import asyncio, logging

from aiogram import Bot, Dispatcher, types, F

from aiogram.filters.command import Command
from aiogram.client.default  import DefaultBotProperties
from aiogram.utils.keyboard  import InlineKeyboardBuilder

from config   import bot_config
from database import Database

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

logging.basicConfig(level = logging.INFO)

bot = Bot(token   = bot_config.bot_token.get_secret_value(),
          default = DefaultBotProperties(parse_mode      = bot_config.parse_mode,
                                         protect_content = bot_config.protect_content))

dp = Dispatcher()
db: Database = None # Can't initialize db here, because `https://stackoverflow.com/questions/64679139/nameerror-name-open-is-not-defined-when-trying-to-log-to-files`

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@dp.message(Command("start"))
async def start_command(message: types.Message):
    builder = InlineKeyboardBuilder()

    for position in bot_config.positions:
        builder.add(types.InlineKeyboardButton(
            text = position,
            callback_data = position)
        )

    await message.answer(
        "Выберите должность",
        reply_markup = builder.as_markup()
    )

@dp.callback_query(F.data.in_(bot_config.positions))
async def assign_position(callback: types.CallbackQuery):
    db.change_characteristic(callback.from_user.username, "Должность", callback.data)

    await callback.answer(
        text = "Спасибо, ваша должность записана!",
        show_alert = True
    )

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

async def main():
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    db = Database("users.db")

    asyncio.run(main())

    del db

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
