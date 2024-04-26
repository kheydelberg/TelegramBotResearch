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
        BotCommand(
            command='cancel',
            description='Сбросить'
        ),
        BotCommand (
            command = 'form',
            description = 'Начать опрос'
        ),
        BotCommand (
            command = 'add_material',
            description = 'Добавить обучающий материал в БД бота'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault()) # скоуп может быть разным только для админов в том числе