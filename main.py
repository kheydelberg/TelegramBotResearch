from aiogram import Bot, Dispatcher
from aiogram.types import ContentType
from core.handlers.basic import get_choose_subject, get_start
import asyncio
import logging
from aiogram import F
from core.settings import settings
from core.utils.commands import set_commands
from aiogram.filters import Command
# from core.handlers.basic import get_location
from core.handlers.basic import get_inline
# from core.handlers.basic import get_photo
from core.handlers.callback import get_contact
from core.handlers.callback import get_geo
from core.handlers.callback import get_math, get_prog


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )

    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    await set_commands(bot)

    dp = Dispatcher()
    # dp.message.register(get_location, F.content_type == ContentType.LOCATION)
    # dp.message.register(get_contact, F.content_type == ContentType.CONTACT)
    dp.callback_query.register(get_geo, F.data == 'geo')
    dp.callback_query.register(get_contact, F.data == 'contact')
    dp.callback_query.register(get_prog, F.data == 'prog')
    dp.callback_query.register(get_math, F.data == 'math')
    dp.message.register(get_choose_subject, Command(commands='subject'))
    dp.message.register(get_inline, Command(commands='inline'))
    dp.message.register(get_start, Command(commands=['start', 'run']))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
