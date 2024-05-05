from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import LEXICON


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
    keyboard_builder.button(text='Геометрия и топология', callback_data='git')
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


def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    keyboard_builder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    keyboard_builder.row(*[InlineKeyboardButton(
        text=LEXICON[button] if button in LEXICON else button,
        callback_data=button) for button in buttons])

    return keyboard_builder.as_markup()
