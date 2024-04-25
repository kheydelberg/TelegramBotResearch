from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await bot.send_message(
        message.from_user.id, f'Привет, <b>{message.from_user.first_name}</b>!'
        )
    await message.answer(f'Привет, <u>{message.from_user.first_name}</u>!')
    await message.reply(
        f'Привет, <tg-spoiler>{message.from_user.first_name}</tg-spoiler>!'
        )


async def get_photo(message: Message, bot: Bot):
    await message.answer('Круто, картинка! Я ее себе сохраню)))')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')
