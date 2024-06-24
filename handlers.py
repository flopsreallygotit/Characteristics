from aiogram import Router

from aiogram.types   import Message
from aiogram.filters import Command

from database import db

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

router = Router()

def get_arguments(text: str) -> dict:
    return dict(map(lambda *args: args, 
                    ["command", "username", "characteristic", "value"], # TODO Looks cringy
                    text.split()))

@router.message(Command("add"))
async def add(message: Message):
    arguments = get_arguments(message.text)
    
    db.change_characteristic(arguments["username"],
                             arguments["characteristic"],
                             arguments["value"])
    
    await message.reply("Characteristic saved!")
    
    db.save_database() # TODO Save with frequency + Del fix

@router.message(Command("show"))
async def add(message: Message):
    arguments = get_arguments(message.text)

    characteristics = db.receive_characteristics(arguments["username"])
    await message.reply(characteristics)
    
    db.save_database()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
