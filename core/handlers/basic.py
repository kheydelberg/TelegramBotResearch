import types
from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import get_Math_Prog
from lexicon.lexicon import LEXICON


async def get_start(message: Message, bot: Bot):
    await message.answer(LEXICON[message.text],reply_markup=get_Math_Prog())
    return True


async def get_help(message: Message, bot: Bot):
    await message.answer(LEXICON[message.text])


async def get_choose_subject(message: Message, bot: Bot):
    await message.answer('Давай выберем предмет!', reply_markup=get_Math_Prog())
