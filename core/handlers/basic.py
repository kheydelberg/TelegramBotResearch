import types
from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import get_Math_Prog
from lexicon.lexicon import LEXICON

import json
from . import apsched
from core.utils.dbconnect import Request
from .STATISTIC import statistics

import os
import codecs




async def get_start(message: Message, bot: Bot):
    await message.answer(LEXICON[message.text],reply_markup=get_Math_Prog())


async def get_help(message: Message, bot: Bot):
    await message.answer(LEXICON[message.text])



async def get_choose_subject(message: Message, bot: Bot):
    await message.answer('Давай выберем предмет!', reply_markup=get_Math_Prog())

async def test(message: Message, bot: Bot, request: Request):
    # await apsched.reset_statistic(request)
    await message.answer('test')
    print(statistics)
    print(int(len(statistics["user_requests"].keys())))
    

