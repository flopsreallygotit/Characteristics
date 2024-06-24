from aiogram import Router

from aiogram.types   import Message, InlineKeyboardButton
from aiogram.filters import Command

from aiogram.utils.keyboard import InlineKeyboardBuilder

from database import db

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    builder = InlineKeyboardBuilder().add(
        InlineKeyboardButton(text = "GitHub", url = "https://github.com/flopsreallygotit")
        )
    
    await message.answer("More info about this bot:", 
                         reply_markup = builder.as_markup())

@router.message(Command("add"))
async def add(message: Message):
    command, username, characteristic, value = message.text.split()
    
    db.change_characteristic(username, characteristic, value)
    
    await message.reply("Characteristic saved!")
    
    db.save_database() # TODO Save with frequency

@router.message(Command("show"))
async def show(message: Message):
    command, username = message.text.split()

    characteristics = db.receive_characteristics(username)
    await message.reply(characteristics)
    
    db.save_database()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
