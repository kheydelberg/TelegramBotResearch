from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, а ты знал, что <b>Это send_message</b> ")
    await message.answer(f"Это message.answer")
    await message.reply(f"Это message.reply")
    await bot.send_message(message.from_user.id,
                           f"Твой id: {message.from_user.id}", reply_markup=get_reply_keyboard())


async def get_location(message: Message, bot: Bot):
    await message.answer(f'Ты отправил геолокацию!\r\a {message.location.latitude}\r\n{message.location.longitude}')

async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отлично, ты отправил картинку! Я сохраню ее себе')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo' + str(file.file_id) + '.jpg')

async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И тебе привет!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)

async def get_secret(message: Message, bot: Bot):
    await message.answer(f'<tg-spoiler> Нефедов ПИДАРАС, ПИДАРАСИНА</tg-spoiler>')

