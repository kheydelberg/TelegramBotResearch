from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Запуск бота'
        ),
        BotCommand(
            command='subject',
            description='Выбрать предмет'
        ),
        BotCommand(
            command='help',
            description='Cправка по работе бота'
        ),
        BotCommand(command='test', description='Тестирование'),
        BotCommand(
            command='test_pagination',
            description='проверка пагинации'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
