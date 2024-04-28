from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from core.handlers.basic import get_start
import asyncio
import logging
from aiogram import F
from core.settings import settings
from core.utils.commands import set_commands
from aiogram.filters import Command
from core.handlers.basic import get_location, get_contact


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )

    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    await set_commands(bot)

    dp = Dispatcher()
    # dp.message.register(get_location, ContentTypeFilter(content_types=[ContentType.LOCATION]))
    dp.message.register(get_location, F.content_type == ContentType.LOCATION)
    dp.message.register(get_contact, F.content_type == ContentType.CONTACT)
    dp.message.register(get_start, Command(commands=['start']))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
