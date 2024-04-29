from aiogram import Bot
from aiogram.types import CallbackQuery

# def select_btn(call: CallbackQuery, bot: Bot):


async def get_geo(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы нажали на кнопку геопозиция')


async def get_contact(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы нажали нв кнопку контакт')
