from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.keyboards.inline_keyboard import get_inline_keyboard
from core.utils.statesform import StepsForm
from aiogram.types import Message, CallbackQuery


async def start_show_feedbacks(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, Введите количество фидбеков, которые хотите посмотреть')
    await state.set_state(StepsForm.GET_NUMBER_FB)
    
async def get_number_str(message: Message, state: FSMContext):
    await message.answer(f'Количество фидбеков для просмотра:\r\n{message.text}\r\n', reply_markup=get_inline_keyboard())
    await state.set_state(StepsForm.CHECK_NUMBER_FB)
    await state.update_data(number=message.text)

async def check_number_str(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if (call.data.endswith('yes')):
       await call.message.answer(f'Отлично, Вы подтвердили количество фидбеков для просмотра')
       await state.set_state(StepsForm.VALIDATE_NUMBER_FB)
       await validate_number_show_feedbacks(call.message, state)
    if (call.data.endswith('no')):
        await call.message.answer("Введите повторно количество фидбеков")
        await state.set_state(StepsForm.GET_NUMBER_FB)

async def validate_number_show_feedbacks(message: Message, state: FSMContext):
    # функиця валидации типа
    await message.answer(f'провалидировали все норм или нет)))')
    await state.set_state(StepsForm.SHOW_FEEDBACKS)
    await message.answer(f'Наши шедевро фидбеки')
    # функция, которая показывает фидбеки
    await state.clear()
    