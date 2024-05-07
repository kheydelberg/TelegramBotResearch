from aiogram.types import Message
from aiogram.types import Message

async def load_backup(message: Message):
    # функция, которая загружает бэкап, подробностей пока нет))
    await message.answer(f'{message.from_user.first_name}, Бэкап тип загружен')
