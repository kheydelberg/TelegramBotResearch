from aiogram import Bot, Dispatcher
import asyncio
from aiogram.types import Message
token = '7183898339:AAFuMXY8XwiVHTjQy_P6I1sO8rpB32s10qE'


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет, дебил {message.from_user.first_name}, как твои дела')
    await message.answer(f'Привет, дебил {message.from_user.first_name}, как твои дела')
    await message.reply(f'Привет, дебил {message.from_user.first_name}, как твои дела')
async def start():
    bot = Bot(token=token)

    dp = Dispatcher()
    dp.message.register(get_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__MMD_file__":
    asyncio.run(start())




