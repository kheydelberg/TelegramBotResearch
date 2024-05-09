from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard_author():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='ФИО', callback_data='fio')
    keyboard_builder.button(text='Никнейм', callback_data='nickname')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()