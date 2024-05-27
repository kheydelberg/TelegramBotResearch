import asyncio
from aiogram import Bot
from aiogram.types import Message
from aiogram.types import CallbackQuery
from core.handlers.basic import get_books_list
from core.keyboards.reply import create_pagination_keyboard, do_you_like, get_Math_Prog, get_category_of_math, get_category_of_prog, pagination_keyboard
from lexicon.lexicon import LEXICON, LEXICON_FOR_FUNC, LEXICON_FOR_SUBJECTS

from core.utils.dbconnect import Request

from data_base import books_database
from config import decrement_current_page, get_current_page, get_books_per_page, increment_current_page



async def category_search(category: str, request: Request):
    return await request.category_search(category)


async def book_callback_handler(callback_query: CallbackQuery):
    book_id = int(callback_query.data.split("_")[1])
    await callback_query.message.answer(f"Вы выбрали: {books_database[book_id]}")
    await callback_query.answer()


async def prev_page_callback_handler(callback_query: CallbackQuery):
    if get_current_page() > 1:
        decrement_current_page()
        await callback_query.message.edit_text(
            text=get_books_list(get_current_page()),
            reply_markup=pagination_keyboard()
        )
    await callback_query.answer()

async def next_page_callback_handler(callback_query: CallbackQuery):
    max_page = (len(books_database) - 1) // get_books_per_page() + 1
    if get_current_page() < max_page:
        increment_current_page()
        await callback_query.message.edit_text(
            text=get_books_list(get_current_page()),
            reply_markup=pagination_keyboard()
        )
    await callback_query.answer()



# Выбор математики
async def get_math(call: CallbackQuery):
    await call.answer()
    await call.message.answer(LEXICON_FOR_SUBJECTS[call.data], reply_markup=get_category_of_math())

# Назад к списку предмета
async def get_back_math(call: CallbackQuery):
    await call.answer()
    await call.message.answer(LEXICON_FOR_SUBJECTS[call.data], reply_markup=get_Math_Prog())

# Выбор подкатегории
async def get_matan(call: CallbackQuery, request: Request):
    await call.answer()
    data = await category_search(category=LEXICON_FOR_FUNC[call.data], request=request)
    print(data)
    text = ''
    for i in range(len(data)):
        text += f"{i+1}. {data[i]['name']}, {data[i]['authors']}\n"
    await call.message.answer(text,
                              reply_markup=pagination_keyboard())
    # await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_linal(call: CallbackQuery, request: Request):
    await call.answer()
    data = await category_search(category=LEXICON_FOR_FUNC[call.data], request=request)
    print(data)
    text = ''
    for i in range(len(data)):
        text += f"{i+1}. {data[i]['name']}, {data[i]['authors']}\n"
    await call.message.answer(text,
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_discra(call: CallbackQuery, request: Request):
    await call.answer()
    data = await category_search(category=LEXICON_FOR_FUNC[call.data], request=request)
    print(data)
    text = ''
    for i in range(len(data)):
        text += f"{i+1}. {data[i]['name']}, {data[i]['authors']}\n"
    await call.message.answer(text,
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_git(call: CallbackQuery, request: Request):
    await call.answer()
    data = await category_search(category=LEXICON_FOR_FUNC[call.data], request=request)
    print(data)
    text = ''
    for i in range(len(data)):
        text += f"{i+1}. {data[i]['name']}, {data[i]['authors']}\n"
    await call.message.answer(text,
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_diffur(call: CallbackQuery, request: Request):
    await call.answer()
    data = await category_search(category=LEXICON_FOR_FUNC[call.data], request=request)
    print(data)
    text = ''
    for i in range(len(data)):
        text += f"{i+1}. {data[i]['name']}, {data[i]['authors']}\n"
    await call.message.answer(text,
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_twims(call: CallbackQuery, request: Request):
    await call.answer()
    data = await category_search(category=LEXICON_FOR_FUNC[call.data], request=request)
    print(data)
    text = ''
    for i in range(len(data)):
        text += f"{i+1}. {data[i]['name']}, {data[i]['authors']}\n"
    await call.message.answer(text,
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


# Выбор программирования
async def get_prog(call: CallbackQuery):
    await call.answer()
    await call.message.answer(LEXICON_FOR_SUBJECTS[call.data], reply_markup=get_category_of_prog())

# Назад к списку предмета
async def get_back_prog(call: CallbackQuery):
    await call.answer()
    await call.message.answer(LEXICON_FOR_SUBJECTS[call.data], reply_markup=get_Math_Prog())

# Выбор подкатегории
async def get_C_plusplus(call: CallbackQuery, request: Request):
    await call.answer()
    data = await category_search(category=LEXICON_FOR_FUNC[call.data], request=request)
    print(data)
    text = ''
    for i in range(len(data)):
        text += f"{i+1}. {data[i]['name']}, {data[i]['authors']}\n"
    await call.message.answer(text,
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_C_sharp(call: CallbackQuery, request: Request):
    await call.answer()
    data = await category_search(category=LEXICON_FOR_FUNC[call.data], request=request)
    print(data)
    text = ''
    for i in range(len(data)):
        text += f"{i+1}. {data[i]['name']}, {data[i]['authors']}\n"
    await call.message.answer(text,
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_python(call: CallbackQuery, request: Request):
    await call.answer()
    data = await category_search(category=LEXICON_FOR_FUNC[call.data], request=request)
    print(data)
    text = ''
    for i in range(len(data)):
        text += f"{i+1}. {data[i]['name']}, {data[i]['authors']}\n"
    await call.message.answer(text,
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_java(call: CallbackQuery, request: Request):
    await call.answer()
    data = await category_search(category=LEXICON_FOR_FUNC[call.data], request=request)
    print(data)
    text = ''
    for i in range(len(data)):
        text += f"{i+1}. {data[i]['name']}, {data[i]['authors']}\n"
    await call.message.answer(text,
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())
