from aiogram import Bot
from aiogram.types import Message
import json
from . import apsched
from core.utils.dbconnect import Request
from .STATISTIC import statistics

import os
import codecs



async def get_start(message: Message, bot: Bot, request: Request):
    await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, а ты знал, что <b>Это send_message</b> ")


async def get_location(message: Message, bot: Bot):
    await message.answer(f'Ты отправил геолокацию!\r\a {message.location.latitude}\r\n{message.location.longitude}')

async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отлично, ты отправил картинку! Я сохраню ее себе')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo' + str(file.file_id) + '.jpg')

    
async def test(message: Message, bot: Bot, request: Request):
    # await apsched.reset_statistic(request)
    await message.answer('test')
    print(statistics)
    print(int(len(statistics["user_requests"].keys())))
    
    
