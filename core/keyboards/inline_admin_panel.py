from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_admin_panel():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Помощь', callback_data='help_admin')
    keyboard_builder.button(text='Посмотреть базу данных', callback_data='show_db')
    keyboard_builder.button(text='Добавить материал', callback_data='add_material')
    keyboard_builder.button(text='Удалить материал по ID', callback_data='delete_material_id')
    keyboard_builder.button(text='Посмотреть фидбеки', callback_data='show_feedbacks')
    keyboard_builder.button(text='Посмотреть необработанные фидбеки', callback_data='show_raw_feedbacks')
    keyboard_builder.button(text='Поменять статус фидбека', callback_data='changing_feedback_status')
    keyboard_builder.button(text='Посмотреть статистику', callback_data='show_statistic')
    keyboard_builder.button(text='Сделать бэкап БД', callback_data='make_backup')
    keyboard_builder.button(text='Загрузить бэкап БД', callback_data='load_backup')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()