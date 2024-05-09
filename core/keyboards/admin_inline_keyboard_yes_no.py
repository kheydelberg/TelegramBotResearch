from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_keyboard_yes_no():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Да', callback_data='yes')
    keyboard_builder.button(text='Нет', callback_data='no')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()