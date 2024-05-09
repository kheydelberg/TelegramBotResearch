from aiogram.types import Message


async def make_backup(message: Message):
    # функция, которая делает бэкап, подробностей пока нет))
    await message.answer(f'{message.from_user.first_name}, Бэкап тип сделан')
