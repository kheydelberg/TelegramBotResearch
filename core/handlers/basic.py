from aiogram import Bot
from aiogram.types import Message


# Функция для обработки команды /start
async def get_start(message: Message, bot: Bot, counter: str):
    await message.answer(f'Сообщение #{counter}')
    # Отправка приветственного сообщения с использованием различных тегов форматирования
    await bot.send_message(message.from_user.id, f'<b>Привет, дебил {message.from_user.first_name}, как твои дела</b>')
    await message.answer(f'<s>Привет, дебил {message.from_user.first_name}, как твои дела</s>')  # Ответ с использованием тега <s>
    await message.reply(f'<tg-spoiler>Привет, дебил {message.from_user.first_name}, как твои дела</tg-spoiler>')  # Ответ с использованием тега <tg-spoiler>