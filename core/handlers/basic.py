from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import inline_keyboard_test
from core.keyboards.reply import get_inline_keyboard, get_Math_Prog


async def get_start(message: Message, bot: Bot):
    await message.answer(f'Привет, <b>{message.from_user.first_name}</b>!',
                         reply_markup=get_inline_keyboard())


async def get_choose_subject(message: Message, bot: Bot):
    await message.answer('Давай выберем предмет!', reply_markup=get_Math_Prog())


# async def get_location(message: Message, bot: Bot):
#     await message.answer(f'Ты отправил геолокацию\r\a'
#                          f'{message.location.latitude}\r\n{message.location.longitude}')


async def get_contact(message: Message, bot: Bot):
    await message.answer(f'Ты отправил телефон.\r\a'
                         f'{message.contact}')



async def get_inline(message: Message, bot: Bot):
    await message.answer(f'Привет, {message.from_user.first_name}, вот инлайн кнопки!',
                         reply_markup=get_inline_keyboard())
