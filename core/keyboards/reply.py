from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import KeyboardButtonPollType


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
