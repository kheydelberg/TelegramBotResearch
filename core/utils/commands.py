from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Запуск бота'
        ),
        BotCommand(
            command='heeeeeelp',
            description='Помощь'
        ),
        BotCommand(
            command='inline',
            description='Показать инлайн кнопки'
        ),
        BotCommand(
            command='subject',
            description='Выбрать предмет'
        )
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
