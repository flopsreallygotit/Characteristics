from aiogram import Router

from aiogram.types   import Message, InlineKeyboardButton
from aiogram.filters import Command

from aiogram.enums.parse_mode import ParseMode
from aiogram.utils.keyboard   import InlineKeyboardBuilder

from database import db
from config   import bot_config

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

router  = Router()
counter = 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def check_for_db_save() -> None:
    global counter

    counter += 1

    if counter % bot_config.frequency == 0:
        db.save_database()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@router.message(Command("start"))
async def start(message: Message):
    builder = InlineKeyboardBuilder().add(
        InlineKeyboardButton(text = "GitHub", url = "https://github.com/flopsreallygotit")
        )
    
    await message.answer("More info about this bot:", 
                         reply_markup = builder.as_markup())
    
    check_for_db_save()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@router.message(Command("add"))
async def add(message: Message):
    command, username, characteristic, value = message.text.split()
    
    db.change_characteristic(username, characteristic, value)
    
    await message.reply("Characteristic saved!")
    
    check_for_db_save()

@router.message(Command("show"))
async def show(message: Message):
    command, username = message.text.split()

    characteristics = db.receive_characteristics(username)
    await message.reply(f"```json\n{characteristics}\n```", 
                        parse_mode = ParseMode.MARKDOWN)
    
    check_for_db_save()

# TODO Add clear command, bind for id

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
