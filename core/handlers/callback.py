from aiogram.types import CallbackQuery
from core.keyboards.reply import get_Math_Prog, get_category_of_math, get_category_of_prog


async def get_geo(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы нажали на кнопку геопозиция')

async def get_contact(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы нажали на кнопку контакт')

# Выбор математики
async def get_math(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы выбрали Высшую математику\n\nВыберите категорию:', reply_markup=get_category_of_math())

# Назад к списку предмета
async def get_back_math(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Давай выберем предмет!', reply_markup=get_Math_Prog())

# Выбор подкатегории
async def get_matan(call: CallbackQuery):
    await call.answer()
    await call.message.answer(f'Вы выбрали <i>Математический анализ</i>\n\nВот, что нашлось по вашему запросу:')

async def get_linal(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы выбрали <i>Линейную алгебру</i>\n\nВот, что нашлось по вашему запросу:')

async def get_discra(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы выбрали <i>Дискретную математику</i>\n\nВот, что нашлось по вашему запросу:')

async def get_git(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы выбрали <i>Геометрию и топологию</i>\n\nВот, что нашлось по вашему запросу:')

async def get_diffur(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы выбрали <i>Дифференцциальные уравнения</i>\n\nВот, что нашлось по вашему запросу:')

async def get_twims(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        'Вы выбрали <i>Теорию вероятности и математическую статистику</i>\n\nВот, что нашлось по вашему запросу:'
        )

# Выбор программирования
async def get_prog(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы выбрали Программирование\n\nВыберите категорию:', reply_markup=get_category_of_prog())

# Назад к списку предмета
async def get_back_prog(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Давай выберем предмет!', reply_markup=get_Math_Prog())

# Выбор подкатегории
async def get_C_plusplus(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        'Вы выбрали <i>C++</i>\n\nВот, что нашлось по вашему запросу:')

async def get_C_sharp(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        'Вы выбрали <i>C#</i>\n\nВот, что нашлось по вашему запросу:')

async def get_python(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        'Вы выбрали <i>Python</i>\n\nВот, что нашлось по вашему запросу:')

async def get_java(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        'Вы выбрали <i>Java</i>\n\nВот, что нашлось по вашему запросу:')
