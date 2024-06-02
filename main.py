import codecs

from aiogram.types import User
from core.utils.dbconnect import Request
from typing import Text
from aiogram import Bot, Dispatcher
from core.handlers.basic import get_choose_subject, get_help, get_start, pagination
import asyncio
import logging
from core.state.user import UserState
import aiomysql

from aiogram.fsm.storage.redis import RedisStorage
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler_di import ContextSchedulerDecorator

from core.handlers.basic import get_start, test
from core.settings import Setting
from aiogram.filters import Command, CommandStart

from aiogram import F
from core.utils.commands import set_commands

from aiogram.filters import Command
from core.handlers.callback import book_callback_handler, get_C_plusplus, get_C_sharp, get_back_math, get_back_prog, get_choose_subject2, get_diffur, like, next_page_callback_handler, notlike, prev_page_callback_handler
from core.handlers.callback import get_discra, get_git, get_java, get_linal, get_matan, get_python, get_twims
from core.handlers.callback import get_math, get_prog

from core.middlewares.dbmiddleware import DBSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.handlers import apsched
from datetime import datetime, timedelta



async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(Setting.bots.admin_id,
                           f"Бот запущен!!!")
    print('Бот запущен!!!\n\n\n')
    

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
            db='sys',
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
            password=f'{Setting.bots.db_password}',
            db='ResearchBot',
            autocommit=True,
            )

async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )

    bot = Bot(token=Setting.bots.bot_token, parse_mode='HTML')


    await set_commands(bot)


    pool_connect = await create_pool()
    
    async with pool_connect.acquire() as connect:
        tmp = Request(connect)
        class_stat = apsched.STAT(tmp)


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
    scheduler.ctx.add_instance(class_stat, declared_class=apsched.STAT)
    scheduler.add_job(apsched.reset_statistic2, trigger='cron', hour=23, minute=59, start_date=datetime.now())
    scheduler.start()


    # dp.update.middleware.register(SchedulerMiddleware(scheduler))
    dp.update.middleware.register(DBSession(pool_connect))
    dp.message.middleware.register(apsched.statistics_middleware())
    
    dp.callback_query.register(get_prog, F.data == 'prog')
    dp.callback_query.register(get_math, F.data == 'math')
    
    
    # dp.callback_query.register(get_linal, F.data == 'linal')
    # dp.callback_query.register(get_discra, F.data == 'discra')
    # dp.callback_query.register(get_git, F.data == 'git')
    # dp.callback_query.register(get_diffur, F.data == 'diffur')
    # dp.callback_query.register(get_twims, F.data == 'twims')

    # dp.callback_query.register(get_C_plusplus, F.data == 'C++')
    # dp.callback_query.register(get_C_sharp, F.data == 'C#')
    # dp.callback_query.register(get_python, F.data == 'python')
    # dp.callback_query.register(get_java, F.data == 'java')
    dp.callback_query.register(get_back_math, F.data == 'back_math')
    dp.callback_query.register(get_back_prog, F.data == 'back_prog')

    dp.callback_query.register(book_callback_handler, F.data.startswith("book_"))
    dp.callback_query.register(prev_page_callback_handler, F.data == 'prev_page')
    dp.callback_query.register(next_page_callback_handler, F.data == 'next_page')
    dp.callback_query.register(get_choose_subject2, F.data =='back_to_choice')
    dp.callback_query.register(like, F.data == 'like')
    dp.callback_query.register(notlike, F.data == 'not_like')
    dp.callback_query.register(get_matan, UserState.PICK_LINK)
    

    dp.message.register(pagination, Command(commands='test_pagination'))
    dp.message.register(get_choose_subject, Command(commands='subject'))
    dp.message.register(get_help, Command(commands='help'))
    dp.message.register(get_start, Command(commands=['start', 'run']))

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(test, Command(commands='test'))
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
