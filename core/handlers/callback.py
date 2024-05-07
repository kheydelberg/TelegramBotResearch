from aiogram import Bot
from aiogram.types import Message
from aiogram.types import CallbackQuery
from core.keyboards.reply import create_pagination_keyboard, do_you_like, get_Math_Prog, get_category_of_math, get_category_of_prog
from lexicon.lexicon import LEXICON, LEXICON_FOR_FUNC, LEXICON_FOR_SUBJECTS


async def category_search(category: str):
    return (f'Тут вызвалась функция cо списком предметов категории {category}')


# Выбор математики
async def get_math(call: CallbackQuery):
    await call.answer()
    await call.message.answer(LEXICON_FOR_SUBJECTS[call.data], reply_markup=get_category_of_math())

# Назад к списку предмета
async def get_back_math(call: CallbackQuery):
    await call.answer()
    await call.message.answer(LEXICON_FOR_SUBJECTS[call.data], reply_markup=get_Math_Prog())

# Выбор подкатегории
async def get_matan(call: CallbackQuery):
    await call.answer()
    await call.message.answer(await category_search(category=LEXICON_FOR_FUNC[call.data]),
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_linal(call: CallbackQuery):
    await call.answer()
    await call.message.answer(await category_search(category=LEXICON_FOR_FUNC[call.data]),
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_discra(call: CallbackQuery):
    await call.answer()
    await call.message.answer(await category_search(category=LEXICON_FOR_FUNC[call.data]),
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_git(call: CallbackQuery):
    await call.answer()
    await call.message.answer(await category_search(category=LEXICON_FOR_FUNC[call.data]),
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_diffur(call: CallbackQuery):
    await call.answer()
    await call.message.answer(await category_search(category=LEXICON_FOR_FUNC[call.data]),
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_twims(call: CallbackQuery):
    await call.answer()
    await call.message.answer(await category_search(category=LEXICON_FOR_FUNC[call.data]),
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
async def get_C_plusplus(call: CallbackQuery):
    await call.answer()
    await call.message.answer(await category_search(category=LEXICON_FOR_FUNC[call.data]),
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_C_sharp(call: CallbackQuery):
    await call.answer()
    await call.message.answer(await category_search(category=LEXICON_FOR_FUNC[call.data]),
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_python(call: CallbackQuery):
    await call.answer()
    await call.message.answer(await category_search(category=LEXICON_FOR_FUNC[call.data]),
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_java(call: CallbackQuery):
    await call.answer()
    await call.message.answer(await category_search(category=LEXICON_FOR_FUNC[call.data]),
                              reply_markup=create_pagination_keyboard('backward','какая страница/из скольки','forward'))
    await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())
