from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard


async def get_start(message: Message, bot: Bot):
    await message.answer(f'Привет, <b>{message.from_user.first_name}</b>!',
                         reply_markup=loc_tel_poll_keyboard)


async def get_location(message: Message, bot: Bot):
    await message.answer(f'Ты отправил геолокацию\r\a'
                         f'{message.location.latitude}\r\n{message.location.longitude}')


async def get_contact(message: Message, bot: Bot):
    await message.answer(f'Ты отправил телефон.\r\a'
                         f'{message.contact}')


async def get_photo(message: Message, bot: Bot):
    await message.answer('Круто, картинка! Я ее себе сохраню)))')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')
