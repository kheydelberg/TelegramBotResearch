from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import KeyboardButtonPollType
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Отправить геолокацию',
            callback_data='geo'
        )
    ],
    [
        InlineKeyboardButton(
            text='Отпрвить телефон',
            callback_data='contact'
        )
    ]
])


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Отправить геолокацию', callback_data='geo')
    keyboard_builder.button(text='Отпрвить телефон', callback_data='contact')

    keyboard_builder.adjust(2)

    return keyboard_builder.as_markup()

def get_Math_Prog():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Высшая математика', callback_data='math')
    keyboard_builder.button(text='Программирование', callback_data='prog')

    keyboard_builder.adjust(2)

    return keyboard_builder.as_markup()

def get_category_of_math():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Математический анализ', callback_data='matan')
    keyboard_builder.button(text='Линейная алгебра', callback_data='linal')
    keyboard_builder.button(text='Дискретная математика', callback_data='discra')
    keyboard_builder.button(text='Геометрия и топологи', callback_data='git')
    keyboard_builder.button(text='Дифференциальные уравнения', callback_data='diffur')
    keyboard_builder.button(text='Теория вероятности и мат. статистика', callback_data='twims')
    keyboard_builder.button(text='Назад', callback_data='back_math')

    keyboard_builder.adjust(1)

    return keyboard_builder.as_markup()

def get_category_of_prog():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='C++', callback_data='C++')
    keyboard_builder.button(text='C#', callback_data='C#')
    keyboard_builder.button(text='Python', callback_data='python')
    keyboard_builder.button(text='Java', callback_data='java')
    keyboard_builder.button(text='Назад', callback_data='back_prog')

    keyboard_builder.adjust(2, 2)

    return keyboard_builder.as_markup()


# loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
#     [
#         KeyboardButton(
#             text='Отправить геолокацию',
#             request_location=True
#         )
#     ],
#     [
#         KeyboardButton(
#             text='Отправить телефон',
#             request_contact=True
#         )
#     ],
#     [
#         KeyboardButton(
#             text='Создать викторину',
#             request_poll=KeyboardButtonPollType(type='quiz')
#         )
#     ]
# ], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='Тут подсказка по вводу')

# reply_keyboard = ReplyKeyboardMarkup(keyboard=[
#     [
#         KeyboardButton(
#             text='Ряд 1. Кнопка 1'
#         ),
#         KeyboardButton(
#             text='Ряд 1. Кнопка 2'
#         )
#     ],
#     [
#         KeyboardButton(
#             text='Ряд 2. Кнопка 1'
#         )
#     ]
# ], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери одну из кнопок ниже')
