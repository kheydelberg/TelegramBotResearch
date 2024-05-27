import types
from aiogram import Bot
from aiogram.types import Message
from core.keyboards.reply import get_Math_Prog, pagination_keyboard
from lexicon.lexicon import LEXICON
import json
from . import apsched
from core.utils.dbconnect import Request
from .STATISTIC import statistics

import os
import codecs

from data_base import books_database
from config import get_books_per_page, get_current_page


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
    

# Функция для получения списка книг на текущей странице
# def get_books_list(page: int) -> str:
#     books_per_page = get_books_per_page()
#     start_book = (page - 1) * books_per_page + 1
#     end_book = min(page * books_per_page, len(books_database))
#     books_list = [f"{j}. {books_database[i]}" for j, i in enumerate(range(start_book, end_book + 1), start=1)]
#     return "\n".join(books_list)

def get_books_list(page: int) -> str:
    books_per_page = get_books_per_page()
    start_book = (page - 1) * books_per_page + 1
    end_book = min(page * books_per_page, len(books_database))
    books_list = [f"{i - start_book + 1}. {books_database[i]}" for i in range(start_book, end_book + 1)]
    return "\n".join(books_list)

async def pagination(message: Message):
    current_page = get_current_page()
    await message.answer(
        text=get_books_list(current_page),
        reply_markup=pagination_keyboard()
    )

