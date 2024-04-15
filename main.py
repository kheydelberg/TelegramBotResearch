"""
ПЕРВЫЙ УРОК - первый бот
"""

# Импорт необходимых модулей
from aiogram import Bot, Dispatcher, F
import asyncio  
from aiogram.filters import CommandStart 
import logging
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ContentType
from core.handlers.basic import get_start
from core.settings import settings
import json
from typing import Dict
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.commands import set_commands
from core.middlewares.countermiddleware import CounterMiddleware

"""
ВТОРОЙ УРОК - магические фильтры
"""

# Функция для запуска бота
async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен')  # Отправка сообщения о запуске бота

# Функция для остановки бота
async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен')  # Отправка сообщения об остановке бота

async def get(message: Message):
    data_message = message.dict()
    print(json.dumps(data_message, default=str))
    result_data_message = await get_data_message(data_message=data_message)
    for key, value in result_data_message.items():
        print(f'{key} - {value}')
        if isinstance(value, str):
            print(f'Используя magic_filter к данным {key} можно обратиться через F.{key} == "{value}"')
        elif isinstance(value, int):
            print(f'Используя magic_filter к данным {key} можно обратиться через F.{key} == {value}')


async def get_data_message(data_message: Dict, prefix: str = '', sep: str = '.'):
    correct_dict = {}
    for key, value in data_message.items():
        if isinstance(value, Dict):
            correct_dict.update(await get_data_message(data_message=value, prefix=f'{prefix}{key}{sep}'))
        else:
            correct_dict[f'{prefix}{key}'] = value
    return correct_dict

async def get_text(message: Message):
    await message.answer('Вы прислали текст')

async def get_hello(message: Message):
    await message.answer('Привет')

async def get_photo(message: Message):
    await message.answer('Вы прислали фотку')

async def get_animation(message: Message):
    await message.answer('Вы прислали гифку')

async def get_admin_message(message: Message):
    await message.answer('Мне написал один из админов!')

def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Кнопка хихи', callback_data='button_1')
    keyboard_builder.button(text='Кнопка хаха', callback_data='button_2')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

async def get_keyboard(message: Message):
    await message.answer('Вот клавиатура', reply_markup=get_inline_keyboard())

async def call_data(call: CallbackQuery):
    await call.answer()
    result = await get_data_message(data_message=call.dict())
    for key, value in result.items():
        print(f'{key} - {value}')

async def get_button_1(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы нажали кнопку хихи')

async def get_button_2(call: CallbackQuery):
    await call.answer()
    await call.message.answer('Вы нажали кнопку хаха')

"""
1. send_message: Этот метод используется для отправки сообщения пользователю. 
Вы указываете идентификатор чата (обычно идентификатор пользователя) и текст сообщения. 
Это наиболее общий метод отправки сообщений.

2. answer: Этот метод используется для отправки ответа на определенное сообщение. 
Он автоматически адресует сообщение обратно в тот же чат, откуда пришло исходное сообщение. 
Это удобно, когда вы хотите ответить на конкретное сообщение пользователя.

3. reply: Этот метод также используется для отправки ответа на определенное сообщение, 
но он добавляет некоторую дополнительную функциональность. 
Например, он может использоваться для цитирования исходного сообщения, чтобы пользователь мог легко отследить контекст ответа.

В общем, answer и reply используются для ответов на конкретные сообщения, 
тогда как send_message используется для отправки сообщений без привязки к какому-либо конкретному сообщению.
"""

# Основная функция для запуска бота
async def start():
    # Настройка логгирования
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')  # Создание экземпляра класса Bot с указанием токена и режима разметки HTML
    """Вы обращаетесь к диспетчеру (Dispatcher) в боте в нескольких сценариях:
    1. Регистрация обработчиков:
    2. Инициализация состояний:
    3. Запуск и остановка бота:
    4. Маршрутизация событий:
    Короче говоря, вы обращаетесь к диспетчеру в моменты инициализации и настройки бота, а также для обработки входящих запросов и управления его жизненным циклом.
    """

    dp = Dispatcher()  # Создание экземпляра класса Dispatcher
    dp.message.middleware.register(CounterMiddleware())
    dp.message.register(get_start, CommandStart())  # Регистрация обработчика для команды /start
    dp.startup.register(start_bot)  # Регистрация функции запуска бота
    dp.shutdown.register(stop_bot)  # Регистрация функции остановки бота
    dp.callback_query.register(get_button_1, F.data == 'button_1')
    dp.callback_query.register(get_button_2, F.data == 'button_2')
    dp.callback_query.register(call_data)
    #dp.message.register(get_text, F.text)
    dp.message.register(get_hello, F.text.lower().startswith('привет'))
    #dp.message.register(get)
    dp.message.register(get_photo, F.content_type == ContentType.PHOTO)
    dp.message.register(get_animation, F.animation)
    #dp.message.register(get_admin_message, F.from_user.id == settings.bots.admin_id) # можно указать несколько админов # можно комбинировать через лог. выражения
    dp.message.register(get_keyboard, F.text == 'Инлайн')
    try:
        await dp.start_polling(bot)  # Запуск бота с использованием long polling
    finally:
        await bot.session.close()  # Закрытие сессии бота

# Проверка, что скрипт запускается как основной
if __name__ == "__main__":
    asyncio.run(start())  # Выполнение основной функции