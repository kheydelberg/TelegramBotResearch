import types
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from core.keyboards.reply import get_Math_Prog, get_inline_keyboard_yes_no, pagination_keyboard
from core.settings import Setting
from lexicon.lexicon import LEXICON
import json
from . import apsched
from core.utils.dbconnect import Request
from .STATISTIC import statistics

import os
import codecs

from data_base import books_database
from config import get_books_per_page, get_current_page
from openai import OpenAI
import aiohttp
import logging

async def cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Текущая ветка отменена")

# Обработчик текстовых сообщений
async def extract_info(user_input: str):
    task_gpt = f""" Из текста: '{user_input}', выдели автора и дисциплину. 
    Дисциплина может быть задана одним их следующих выражений: 
    'ТВиМС','Матан','ДУ','ЛинАл','Программирование C++','Программирование C#', ' Программирование Python','АлГем','Программирование Java'. 
    У автора может быть или фамилия или фамилия и инициалы через точку. Если дисциплина или автор отсутствуют, считай их пробелом. Если дисциплина или автор отсутствуют, напиши 'отсутствует'.
    Ответ выведи в формате дисциплина: , автор: """
    request_gpt = {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": task_gpt}]}

    async with aiohttp.ClientSession() as session:
        headers = { "Authorization": f"Bearer {Setting.bots.GPT_token}", 
                   "Content-Type": "application/json" } 
        async with session.post('https://api.proxyapi.ru/openai/v1/chat/completions', json=request_gpt, headers=headers) as response: 
            if response.status == 200: 
                response_data = await response.json() 
                answer = response_data['choices'][0]['message']['content'].strip() 
                return answer 
            else: 
                error_message = await response.text()
                logging.error(f"Error {response.status} : {error_message}")
                return f"Произошла ошибка при обращении к API OpenAI. {error_message}"

async def handle(message: Message, state: FSMContext):
    info = await extract_info(message.text)
    await message.reply(info, reply_markup=get_inline_keyboard_yes_no())
    info = info.replace(":", "").replace(",", "").replace(".", "").split()
    print(info)
    if (len(info) > 3):
        cat = info[1]
        aut = info[3]
    else:
        cat = ""
        aut = ""
    await state.update_data(gpt_category = cat)
    await state.update_data(gpt_author = aut)
    await state.set_state()

async def get_start(message: Message, bot: Bot):
    await message.answer(LEXICON[message.text],reply_markup=get_Math_Prog())


async def get_help(message: Message, bot: Bot):
    await message.answer(LEXICON[message.text])



async def get_choose_subject(message: Message, bot: Bot):
    print("HAHA\n\n")
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

