import asyncio
from aiogram import Bot
from aiogram.types import Message
from aiogram.types import CallbackQuery
from core.handlers.basic import get_books_list
from core.keyboards.reply import back_to_choice, create_pagination_keyboard, do_you_like, get_Math_Prog, get_category_of_math, get_category_of_prog, pagination_keyboard
from lexicon.lexicon import LEXICON, LEXICON_FOR_FUNC, LEXICON_FOR_SUBJECTS
from aiogram.fsm.context import FSMContext
from core.utils.dbconnect import Request
from core.state.user import UserState
from data_base import books_database
from config import decrement_current_page, get_current_page, get_books_per_page, increment_current_page


async def agreed(call: CallbackQuery, bot: Bot, state: FSMContext,  request: Request):
    info = await state.get_data()
    print(info)   
    cat = info.get("gpt_category")
    author = info.get("gpt_author")
    if (author == "отсутствует"): author = ""
    if (cat == "отсутствует"): cat = ""

    data = await request.category_author_search(cat, author)
    print(data)
    await state.update_data(lines = data)
    text = ''
    for i in range(len(data)):
        text += f"{i+1}. {data[i]['name']}, {data[i]['authors']}\n"
    if (text == ''):
        await call.message.answer("Ничего не найдено", reply_markup=back_to_choice())
    else:
        await call.message.answer(text,
                              reply_markup=pagination_keyboard(len(data)))

    await call.answer()
    await call.message.delete()

async def not_agreed(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.answer()
    await call.message.delete()
    await start_extract(call, state)
    
            
async def start_extract(call: CallbackQuery, state: FSMContext):
     await call.message.answer(f'Введите запрос на поиск материала в свободной форме:')
     await state.set_state(UserState.GET_GPT_REQUEST)
     await call.answer()


async def like(callback_query: CallbackQuery, state: FSMContext, request: Request):
    context_data = await state.get_data()
    print(context_data)
    link_id = context_data.get("lines")[context_data.get("picked_id")]["idLinks"]
    print(link_id)
    await request.add_like(link_id)
    await callback_query.message.answer("Вы лайкнули!\n")
    await callback_query.answer()
    await callback_query.message.delete()
     

async def notlike(callback_query: CallbackQuery,state: FSMContext, request: Request):
    await callback_query.message.answer("Жаль, будем стараться лучше\n")
    await callback_query.answer()
    await callback_query.message.delete()

async def get_choose_subject2(callback_query: CallbackQuery, bot: Bot):
    await callback_query.answer()
    await callback_query.message.answer('Давай выберем предмет!', reply_markup=get_Math_Prog())

async def category_search(category: str, request: Request):
    return await request.category_search(category)


async def book_callback_handler(callback_query: CallbackQuery, state: FSMContext):
    book_id = int(callback_query.data.split("_")[1]) - 1
    contex_data = await state.get_data()
    data = contex_data.get('lines')
    # picked = data[book_id]["idLinks"]
    await state.update_data(picked_id = book_id)    

    await callback_query.message.answer(f"Вы выбрали: {data[book_id]['name']}\n\n{data[book_id]['link']}", reply_markup=back_to_choice())
    await callback_query.answer()
    await callback_query.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())
    await callback_query.message.delete()


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
async def get_math(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer(LEXICON_FOR_SUBJECTS[call.data], reply_markup=get_category_of_math())
    await state.set_state(UserState.PICK_LINK)

# Назад к списку предмета
async def get_back_math(call: CallbackQuery):
    await call.answer()
    await call.message.answer(LEXICON_FOR_SUBJECTS[call.data], reply_markup=get_Math_Prog())

# Выбор подкатегории
async def get_matan(call: CallbackQuery, request: Request, state: FSMContext):
    await call.answer()
    data = await category_search(category=LEXICON_FOR_FUNC[call.data], request=request)
    print(data)
    await state.update_data(lines = data)
    text = ''
    for i in range(len(data)):
        text += f"{i+1}. {data[i]['name']}, {data[i]['authors']}\n"
    await call.message.answer(text,
                              reply_markup=pagination_keyboard(len(data)))
    state.set_state(UserState.NOT_PICK_LINK)
    # await call.message.answer(LEXICON['text_likes'], reply_markup=do_you_like())


async def get_linal(call: CallbackQuery, request: Request, state: FSMContext):
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
