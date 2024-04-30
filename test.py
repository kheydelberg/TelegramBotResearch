from aiogram import Bot, Dispatcher
import asyncio  
from aiogram.filters import CommandStart, Command 
import logging
from core.handlers.basic import get_start
from core.settings import settings
from core.utils.commands import set_commands
from core.handlers import add_material
from core.handlers import delete_material
from core.handlers import view_db
from core.handlers import view_feedback
from core.handlers import view_raw_feedback
from core.handlers import view_statistic
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

    dp.message.register(delete_material.show_db_to_delete, Command(commands='delete_material_id'))
    dp.message.register(delete_material.get_id, StepsForm.GET_ID)
    dp.message.register(delete_material.delete_material, StepsForm.DELETE_MATERIAL)

    dp.callback_query.register(add_material.check_category, StepsForm.CHECK_CATEGORY)
    dp.callback_query.register(add_material.check_description, StepsForm.CHECK_DESCRIPTION)
    dp.callback_query.register(add_material.check_link, StepsForm.CHECK_LINK)
    dp.callback_query.register(add_material.check_name, StepsForm.CHECK_NAME)
    dp.callback_query.register(add_material.check_author, StepsForm.CHECK_AUTHOR)

    dp.callback_query.register(delete_material.check_id, StepsForm.CHECK_ID)

    dp.message.register(view_db.start_show_db, Command(commands='show_materials'))
    dp.message.register(view_db.get_number_str, StepsForm.GET_NUMBER_DB)
    dp.message.register(view_db.validate_number, StepsForm.VALIDATE_NUMBER_DB)
    dp.message.register(view_db.show_db, StepsForm.SHOW_DB)

    dp.callback_query.register(view_db.check_number_str, StepsForm.CHECK_NUMBER_DB)

    dp.message.register(view_feedback.start_show_feedbacks, Command(commands='show_feedbacks'))
    dp.message.register(view_feedback.get_number_str, StepsForm.GET_NUMBER_FB)
    dp.message.register(view_feedback.validate_number, StepsForm.VALIDATE_NUMBER_FB)
    dp.message.register(view_feedback.show_feedbacks, StepsForm.SHOW_FEEDBACKS)

    dp.callback_query.register(view_feedback.check_number_str, StepsForm.CHECK_NUMBER_FB)

    dp.message.register(view_raw_feedback.start_show_raw_feedbacks, Command(commands='show_raw_feedbacks'))
    dp.message.register(view_raw_feedback.get_number_str, StepsForm.GET_NUMBER_RFB)
    dp.message.register(view_raw_feedback.validate_number, StepsForm.VALIDATE_NUMBER_RFB)
    dp.message.register(view_raw_feedback.show_raw_feedbacks, StepsForm.SHOW_RAW_FEEDBACKS)

    dp.callback_query.register(view_raw_feedback.check_number_str, StepsForm.CHECK_NUMBER_RFB)

    dp.message.register(view_statistic.start_show_statistic, Command(commands='show_statistic'))
    dp.message.register(view_statistic.get_number_str, StepsForm.GET_NUMBER_ST)
    dp.message.register(view_statistic.validate_number, StepsForm.VALIDATE_NUMBER_ST)
    dp.message.register(view_statistic.show_statistic, StepsForm.SHOW_STATISTIC)

    dp.callback_query.register(view_statistic.check_number_str, StepsForm.CHECK_NUMBER_ST)


    try:
        await dp.start_polling(bot)  # Запуск бота с использованием long polling
    finally:
        await bot.session.close()  # Закрытие сессии бота

# Проверка, что скрипт запускается как основной
if __name__ == "__main__":
    asyncio.run(start())  # Выполнение основной функции