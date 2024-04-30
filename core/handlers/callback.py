from aiogram.types import CallbackQuery
from core.keyboards.reply import get_category_of_math, get_category_of_prog


async def get_geo(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы нажали на кнопку геопозиция')

async def get_contact(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы нажали на кнопку контакт')

async def get_math(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы выбрали Высшую математику', reply_markup=get_category_of_math())

async def get_prog(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы выбрали Программирование', reply_markup=get_category_of_prog())
