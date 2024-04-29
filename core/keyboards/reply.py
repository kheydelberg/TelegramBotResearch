from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import KeyboardButtonPollType
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Ряд 1. Кнопка 1'
        ),
        KeyboardButton(
            text='Ряд 1. Кнопка 2'
        )
    ],
    [
        KeyboardButton(
            text='Ряд 2. Кнопка 1'
        )
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери одну из кнопок ниже')


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
    keyboard_builder.button(text='Создать викторину', callback_data='poll')

    keyboard_builder.adjust(2)

    return keyboard_builder.as_markup()


loc_tel_poll_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Отправить геолокацию',
            request_location=True
        )
    ],
    [
        KeyboardButton(
            text='Отправить телефон',
            request_contact=True
        )
    ],
    [
        KeyboardButton(
            text='Создать викторину',
            request_poll=KeyboardButtonPollType(type='quiz')
        )
    ]
], resize_keyboard=True, one_time_keyboard=False, input_field_placeholder='Тут подсказка по вводу')
