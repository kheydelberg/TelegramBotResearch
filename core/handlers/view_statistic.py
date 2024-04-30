from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.keyboards.inline_keyboard import get_inline_keyboard
from core.utils.statesform import StepsForm
from aiogram.types import Message, CallbackQuery
from aiogram import Bot

async def start_show_statistic(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, Введите количество строк, которые хотите посмотреть')
    await state.set_state(StepsForm.GET_NUMBER_ST)
    
async def get_number_str(message: Message, state: FSMContext):
    await message.answer(f'Количество строк БД для просмотра:\r\n{message.text}\r\n', reply_markup=get_inline_keyboard())
    await state.set_state(StepsForm.CHECK_NUMBER_ST)
    await state.update_data(number=message.text)

async def check_number_str(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if (call.data.endswith('yes')):
       await call.message.answer(f'Отлично, Вы подтвердили количество строк для просмотра, подождите немного и количество строк будет провалидировано, хорошо?')
       await state.set_state(StepsForm.VALIDATE_NUMBER_ST)
    if (call.data.endswith('no')):
        await call.message.answer("Введите повторно количество строк")
        await state.set_state(StepsForm.GET_NUMBER_ST)

async def validate_number(message: Message, bot: Bot, state: FSMContext):
    # функиця валидации типа
    await bot.send_message(message.from_user.id, f'провалидировали все норм или нет))), подождите немного и статистика будет выведена, хорошо?')
    await state.set_state(StepsForm.SHOW_STATISTIC)
    

async def show_statistic(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(message.from_user.id, f'Наша шедевро статистика')
    # функция, которая показывает статистику
    await state.clear()