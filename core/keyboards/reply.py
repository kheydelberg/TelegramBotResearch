import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON
from data_base import books_database
from aiogram import Bot, Dispatcher, types
from config import get_current_page, get_books_per_page



def get_inline_keyboard_yes_no():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Да', callback_data='yes')
    keyboard_builder.button(text='Нет', callback_data='no')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()

def get_Math_Prog():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Высшая математика', callback_data='math')
    keyboard_builder.button(text='Программирование', callback_data='prog')
    keyboard_builder.button(text='Свободный запрос', callback_data='gpt_request')

    keyboard_builder.adjust(2, 1)

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


def back_to_choice():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Назад к выбору', callback_data='back_to_choice')

    return keyboard_builder.as_markup()

def do_you_like():
    keyboard_builder= InlineKeyboardBuilder()
    keyboard_builder.button(text= 'Да👌', callback_data='like')
    keyboard_builder.button(text='Нет😒', callback_data='not_like')

    keyboard_builder.adjust(2)

    return keyboard_builder.as_markup()





def pagination_keyboard(size: int) -> InlineKeyboardBuilder:
    current_page = get_current_page()
    books_per_page = get_books_per_page()
    max_page = (size - 1) // books_per_page + 1  # Вычисляем количество страниц
    start_book = (current_page - 1) * books_per_page + 1
    end_book = min(current_page * books_per_page, size)

    keyboard = InlineKeyboardBuilder()

    # Кнопка для перехода на предыдущую страницу
    if current_page > 1:
        keyboard.button(text="<", callback_data="prev_page")

    # Кнопки для книг
    for i in range(start_book, end_book + 1):
        button_text = str(i - start_book + 1)  # Номера на странице начинаются с 1
        keyboard.button(text=button_text, callback_data=f"book_{i}")

    # Кнопка для перехода на следующую страницу
    if current_page < max_page:
        keyboard.button(text=">", callback_data="next_page")

    return keyboard.as_markup()