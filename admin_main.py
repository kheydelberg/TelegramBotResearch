from aiogram import Bot, Dispatcher
import asyncio  
from aiogram.filters import Command 
import logging
from core.admin_handlers.basic import get_start
from core.settings import settings
from core.utils.admin_commands import set_admin_commands
from core.admin_handlers import add_material
from core.admin_handlers import delete_material
from core.admin_handlers import view_db
from core.admin_handlers import view_feedback
from core.admin_handlers import view_raw_feedback
from core.admin_handlers import view_statistic
#from core.admin_handlers import load_backup
#from core.admin_handlers import make_backup
from core.admin_handlers import changing_feedback_status
from core.utils.admin_statesform import StepsForm
from core.admin_handlers import admin_panel



# Функция для запуска бота
async def start_bot(bot: Bot):
    await set_admin_commands(bot)
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

    dp.message.register(get_start, Command(commands='start_admin')) 

    dp.startup.register(start_bot)  # Регистрация функции запуска бота
    dp.shutdown.register(stop_bot)  # Регистрация функции остановки бота

    dp.callback_query.register(admin_panel.admin_panel)

    dp.message.register(add_material.get_category, StepsForm.GET_CATEGORY)
    dp.message.register(add_material.get_description, StepsForm.GET_DESCRIPTION)
    dp.message.register(add_material.get_link, StepsForm.GET_LINK)
    dp.message.register(add_material.get_name, StepsForm.GET_NAME)
    dp.message.register(add_material.get_author, StepsForm.GET_AUTHOR)
    dp.message.register(add_material.get_all_validate, StepsForm.GET_ALL)
    dp.message.register(add_material.add_material, StepsForm.ADD_MATERIAL)

    #dp.message.register(delete_material.show_db_to_delete, Command(commands='delete_material_id'))
    dp.message.register(delete_material.get_id, StepsForm.GET_ID)
    dp.callback_query.register(delete_material.check_id, StepsForm.CHECK_ID)
    dp.message.register(delete_material.validate_id_delete_material, StepsForm.VALIDATE_ID)

    dp.callback_query.register(add_material.check_category, StepsForm.CHECK_CATEGORY)
    dp.callback_query.register(add_material.check_description, StepsForm.CHECK_DESCRIPTION)
    dp.callback_query.register(add_material.check_link, StepsForm.CHECK_LINK)
    dp.callback_query.register(add_material.check_name, StepsForm.CHECK_NAME)
    dp.callback_query.register(add_material.check_author, StepsForm.CHECK_AUTHOR)

    dp.callback_query.register(delete_material.check_id, StepsForm.CHECK_ID)

    #dp.message.register(view_db.start_show_db, Command(commands='show_materials'))
    dp.message.register(view_db.get_number_str, StepsForm.GET_NUMBER_DB)
    dp.message.register(view_db.validate_number_show_db, StepsForm.VALIDATE_NUMBER_DB)

    dp.callback_query.register(view_db.check_number_str, StepsForm.CHECK_NUMBER_DB)

    #dp.message.register(view_feedback.start_show_feedbacks, Command(commands='show_feedbacks'))
    dp.message.register(view_feedback.get_number_str, StepsForm.GET_NUMBER_FB)
    dp.message.register(view_feedback.validate_number_show_feedbacks, StepsForm.VALIDATE_NUMBER_FB)

    dp.callback_query.register(view_feedback.check_number_str, StepsForm.CHECK_NUMBER_FB)

    #dp.message.register(view_raw_feedback.start_show_raw_feedbacks, Command(commands='show_raw_feedbacks'))
    dp.message.register(view_raw_feedback.get_number_str, StepsForm.GET_NUMBER_RFB)
    dp.message.register(view_raw_feedback.validate_number_show_raw_feedbacks, StepsForm.VALIDATE_NUMBER_RFB)
    dp.callback_query.register(view_raw_feedback.check_number_str, StepsForm.CHECK_NUMBER_RFB)

    #dp.message.register(view_statistic.start_show_statistic, Command(commands='show_statistic'))
    dp.message.register(view_statistic.get_number_str, StepsForm.GET_NUMBER_ST)
    dp.callback_query.register(view_statistic.check_number_str, StepsForm.CHECK_NUMBER_ST)
    dp.message.register(view_statistic.validate_number_show_statistic, StepsForm.VALIDATE_NUMBER_ST)

    #dp.message.register(make_backup.make_backup, Command(commands='make_backup'))
    #dp.message.register(load_backup.load_backup, Command(commands='load_backup'))

    #dp.message.register(changing_feedback_status.show_fb_to_changing_fb_status, Command(commands='changing_feedback_status'))
    dp.message.register(changing_feedback_status.get_id_fb, StepsForm.GET_ID_FB)
    dp.callback_query.register(changing_feedback_status.check_id_fb, StepsForm.CHECK_ID_FB)
    dp.message.register(changing_feedback_status.validate_id_change_status, StepsForm.VALIDATE_ID_FB)

    try:
        await dp.start_polling(bot)  # Запуск бота с использованием long polling
    finally:
        await bot.session.close()  # Закрытие сессии бота

# Проверка, что скрипт запускается как основной
if __name__ == "__main__":
    asyncio.run(start())  # Выполнение основной функции