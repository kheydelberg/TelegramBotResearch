from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
        command='start',
        description='Начало работы',
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
         BotCommand (
           command = 'show_materials',
           description = 'Посмотреть обучающие материалы из БД'
        ),
        BotCommand (
            command = 'add_material',
            description = 'Добавить обучающий материал в БД бота'
        ),
        BotCommand (
            command = 'delete_material_id',
            description = 'Удалить обучающий материал по id'
        ),
         BotCommand (
           command = 'show_feedback',
           description = 'Посмотреть все фидбеки'
        ),
         BotCommand (
           command = 'show_raw_feedback',
           description = 'Посмотреть необработанные фидбеки'
        ),
         BotCommand (
           command = 'changing_feedback_status',
           description = 'Поменять статус фидбека'
        ),
         BotCommand (
           command = 'show_satisctics',
           description = 'Посмотреть статистику'
        ),
         BotCommand (
           command = 'make_backup',
           description = 'Сделать бэкап БД'
        ),
         BotCommand (
           command = 'load_backup',
           description = 'Загрузить бэкап БД'
        ),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault()) # скоуп может быть разным только для админов в том числе