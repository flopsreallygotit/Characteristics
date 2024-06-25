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

def check_query_count() -> bool:
    global counter
    counter += 1

    max_query_count = bot_config.max_query_count

    if counter != max_query_count:
        return False
    
    print("Number of queries is equal to max_query_count.")
    counter -= max_query_count

    return True

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@router.message(Command("start"))
async def start(message: Message):
    builder = InlineKeyboardBuilder().add(
        InlineKeyboardButton(text = "GitHub", url = "https://github.com/flopsreallygotit/Characteristics")
        )
    
    await message.answer("More info about this bot:", 
                         reply_markup = builder.as_markup())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@router.message(Command("add"))
async def add(message: Message):
    command, username, characteristic, value = message.text.split() # TODO try except
    
    db.change_characteristic(username, characteristic, value)
    
    await message.reply("Characteristic saved!")
    
    if check_query_count():
        db.save_database()
        print(message.new_chat_members)
        # await message.answer("Notification!")

@router.message(Command("show"))
async def show(message: Message):
    command, username = message.text.split()

    characteristics = db.receive_characteristics(username)
    await message.reply(f"```json\n{characteristics}\n```", 
                        parse_mode = ParseMode.MARKDOWN)

# TODO Add clear command, bind for id

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
