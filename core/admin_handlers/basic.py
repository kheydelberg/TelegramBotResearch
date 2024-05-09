from aiogram import Bot
from aiogram.types import Message
from core.settings import settings
from core.keyboards.inline_admin_panel import get_admin_panel

async def get_start(message: Message, bot: Bot):
    user_id = message.from_user.id
    if user_id == settings.bots.admin_id:
        await bot.send_message(message.from_user.id, f'<b>Привет, {message.from_user.first_name}, я админ панель, которая поможет тебе работать с БД, статистикой, фидбеками </b>', reply_markup=get_admin_panel())
    else:
        await bot.send_message(message.from_user.id, f'<b>Привет, {message.from_user.first_name}, у Вас нет доступа')