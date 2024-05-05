from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import create_pagination_keyboard, get_Math_Prog
from lexicon.lexicon import LEXICON


async def get_start(message: Message, bot: Bot):
    await message.answer(LEXICON[message.text],reply_markup=get_Math_Prog())


async def get_help(message: Message, bot: Bot):
    await message.answer(LEXICON[message.text])


async def get_choose_subject(message: Message, bot: Bot):
    await message.answer('Давай выберем предмет!', reply_markup=get_Math_Prog())


 #@router.message(Command(commands='continue'))
# async def list_of_materials(message: Message, bot: Bot):
#     text = 'Здесь должны подтягиваться списки материалов'
#     await message.answer(
#         text='Здесь должны подтягиваться списки материалов',
#         reply_markup=create_pagination_keyboard(
#             'backward',
#             'какая страница/из скольки',
#             'forward'
#         )
#     )
