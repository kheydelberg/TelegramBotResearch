import codecs
from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
import logging #Блять что это???????????????????????????????????????????
import aiomysql

from aiogram.fsm.storage.redis import RedisStorage
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler_di import ContextSchedulerDecorator

from core.handlers.basic import get_start, get_photo, get_hello, get_location, get_inline, test
from core.handlers.callback import select_macbook
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_true_contact, get_fake_contact
from core.settings import Setting
from aiogram.filters import Command, CommandStart
from aiogram import F
from core.utils.commands import set_commands
from core.utils.callbackdata import MacInfo
from core.handlers.pay import order, pre_checkout_query, successful_payment, shipping_check
from core.middlewares.countermiddleware import CounterMiddleware
from core.middlewares.officehours import OfficeHoursMiddleware
from core.middlewares.apschedulermiddleware import SchedulerMiddleware
from core.middlewares.dbmiddleware import DBSession
from core.handlers import form
from core.utils.statesform import StepsForm
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.handlers import apsched
from datetime import datetime, timedelta


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(Setting.bots.admin_id,
                           f"Бот запущен!!!")
    print('Бот запущен!!!')
    

async def stop_bot(bot: Bot):
    await bot.send_message(Setting.bots.admin_id,
                           f"Бот остановлен!!!")
    print("Бот остановлен!")

async def create_pool():
    try:
        return await aiomysql.create_pool(
            host = 'localhost', 
            port = 3306, 
            user='root',
            password=f'{Setting.bots.db_password}',
            db='ResearchBot',
            autocommit=True,
            )
    except:
        pool = await aiomysql.create_pool(
            host = 'localhost', 
            port = 3306, 
            user='root',
            password=f'{Setting.bots.db_password}',
            db='mydb',
            autocommit=True,
            )
        async with pool.acquire() as connect:
            async with connect.cursor(aiomysql.DictCursor) as cur:
                temp = 'CREATE SCHEMA `researchbot`;'
                await cur.execute(temp)
        return await aiomysql.create_pool(
            host = 'localhost', 
            port = 3306, 
            user='root',
            password='Basek@319_',
            db='ResearchBot',
            autocommit=True,
            )

async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                        "(%(filename)s.%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=Setting.bots.bot_token, parse_mode='HTML')

    pool_connect = await create_pool()

    storage = RedisStorage.from_url('redis://localhost:6379/0')

    dp = Dispatcher(storage=storage)
    
    jobstores = {
        'default': RedisJobStore(jobs_key='dispatched_trips_jobs',
                                 run_times_key='dispatched_trips_running',
                                 host='localhost',
                                 db=2,
                                 port=6379)
        }
    
    scheduler = ContextSchedulerDecorator(AsyncIOScheduler(timezone="Europe/Moscow", jobstores=jobstores))
    scheduler.ctx.add_instance(bot, declared_class=Bot)
    # scheduler.add_job(apsched.send_message_time, trigger='date', run_date= datetime.now() + timedelta(seconds=10))
    # scheduler.add_job(apsched.send_message_cron, trigger='cron', hour=datetime.now().hour, minute= datetime.now().minute + 1, start_date=datetime.now())
    # scheduler.add_job(apsched.send_message_interval, trigger='interval', seconds=60)
    # scheduler.start()


    # dp.message.middleware.register(CounterMiddleware())
    # dp.update.middleware.register(OfficeHoursMiddleware())
    # dp.update.middleware.register(SchedulerMiddleware(scheduler))
    dp.update.middleware.register(DBSession(pool_connect))

    dp.message.register(order, Command(commands='pay'))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment, F.successful_payment)
    dp.shipping_query.register(shipping_check)
    #dp.callback_query.register(select_macbook, F.data.startswith('inline_'))
    #dp.callback_query.register(select_macbook, MacInfo.filter())
    dp.callback_query.register(select_macbook, MacInfo.filter(F.num == 1))
    dp.message.register(get_inline, Command(commands='inline'))
    dp.message.register(get_hello, F.text == 'Привет')
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_start, Command(commands=['start', 'run']))  # CommandStart()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(form.get_form, Command(commands='form'))
    dp.message.register(form.get_name, StepsForm.GET_NAME)
    dp.message.register(form.get_last_name, StepsForm.GET_LAST_NAME)    
    dp.message.register(form.get_age, StepsForm.GET_AGE)

    dp.message.register(test, Command(commands='test'))
    

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())