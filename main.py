from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
import logging #Блять что это???????????????????????????????????????????


from core.handlers.basic import get_start, get_photo, get_hello, get_location, get_secret, get_inline
from core.handlers.callback import select_macbook
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_true_contact, get_fake_contact
from core.settings import Setting
from aiogram.filters import Command, CommandStart
from aiogram import F
from core.utils.commands import set_commands
from core.utils.callbackdata import MacInfo




async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(Setting.bots.admin_id,
                           f"Бот запущен!!!")
    print('Бот запущен!!!')

async def stop_bot(bot: Bot):
    await bot.send_message(Setting.bots.admin_id,
                           f"Бот остановлен!!!")
    print("Бот остановлен!")


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                        "(%(filename)s.%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=Setting.bots.bot_token, parse_mode='HTML')


    dp = Dispatcher()
    #dp.callback_query.register(select_macbook, F.data.startswith('inline_'))
    #dp.callback_query.register(select_macbook, MacInfo.filter())
    dp.callback_query.register(select_macbook, MacInfo.filter(F.num == 1))
    dp.message.register(get_location, F.location)
    dp.message.register(get_inline, Command(commands='inline'))
    dp.message.register(get_hello, F.text == 'Привет')
    dp.message.register(get_secret, F.text == 'Секрет')
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_start, Command(commands=['start', 'run']))  # CommandStart()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)



    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())