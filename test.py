from aiogram import Bot, Dispatcher
import asyncio  
from aiogram.filters import CommandStart, Command 
import logging
from core.handlers.basic import get_start
from core.settings import settings
from core.utils.commands import set_commands
from core.handlers import add_material
from core.utils.statesform import StepsForm



# Функция для запуска бота
async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')  # Отправка сообщения о запуске бота


# Функция для остановки бота
async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')  # Отправка сообщения об остановке бота


# Основная функция для запуска бота
async def start():
    # Настройка логгирования
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')  # Создание экземпляра класса Bot с указанием токена и режима разметки HTML

    dp = Dispatcher()  # Создание экземпляра класса Dispatcher
    dp.message.register(get_start, CommandStart())  # Регистрация обработчика для команды /start
    dp.startup.register(start_bot)  # Регистрация функции запуска бота
    dp.shutdown.register(stop_bot)  # Регистрация функции остановки бота
    dp.message.register(add_material.get_material, Command(commands='add_material'))
    dp.message.register(add_material.get_category, StepsForm.GET_CATEGORY)
    dp.message.register(add_material.get_description, StepsForm.GET_DESCRIPTION)
    dp.message.register(add_material.get_link, StepsForm.GET_LINK)
    dp.message.register(add_material.get_name, StepsForm.GET_NAME)
    dp.message.register(add_material.get_author, StepsForm.GET_AUTHOR)
    dp.message.register(add_material.get_all, StepsForm.GET_ALL)
    dp.message.register(add_material.validate_material, StepsForm.VALIDATE_MATERIAL)

    dp.callback_query.register(add_material.check_category, StepsForm.CHECK_CATEGORY)
    dp.callback_query.register(add_material.check_description, StepsForm.CHECK_DESCRIPTION)
    dp.callback_query.register(add_material.check_link, StepsForm.CHECK_LINK)
    dp.callback_query.register(add_material.check_name, StepsForm.CHECK_NAME)
    dp.callback_query.register(add_material.check_author, StepsForm.CHECK_AUTHOR)



    try:
        await dp.start_polling(bot)  # Запуск бота с использованием long polling
    finally:
        await bot.session.close()  # Закрытие сессии бота

# Проверка, что скрипт запускается как основной
if __name__ == "__main__":
    asyncio.run(start())  # Выполнение основной функции