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
from core.handlers.callback import get_C_plusplus, get_C_sharp, get_back_math, get_back_prog, get_contact, get_diffur
from core.handlers.callback import get_discra, get_git, get_java, get_linal, get_matan, get_python, get_twims
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
    dp.callback_query.register(get_matan, F.data == 'matan')
    dp.callback_query.register(get_linal, F.data == 'linal')
    dp.callback_query.register(get_discra, F.data == 'discra')
    dp.callback_query.register(get_git, F.data == 'git')
    dp.callback_query.register(get_diffur, F.data == 'diffur')
    dp.callback_query.register(get_twims, F.data == 'twims')
    dp.callback_query.register(get_C_plusplus, F.data == 'C++')
    dp.callback_query.register(get_C_sharp, F.data == 'C#')
    dp.callback_query.register(get_python, F.data == 'python')
    dp.callback_query.register(get_java, F.data == 'java')
    dp.callback_query.register(get_back_math, F.data == 'back_math')
    dp.callback_query.register(get_back_prog, F.data == 'back_prog')
    dp.message.register(get_choose_subject, Command(commands='subject'))
    dp.message.register(get_inline, Command(commands='inline'))
    dp.message.register(get_start, Command(commands=['start', 'run']))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
