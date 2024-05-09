from aiogram.fsm.context import FSMContext
from core.keyboards.admin_inline_keyboard_yes_no import get_inline_keyboard_yes_no
from core.utils.admin_statesform import StepsForm
from aiogram.types import Message, CallbackQuery


async def start_show_raw_feedbacks(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, Введите количество необработанных фидбеков, которые хотите посмотреть')
    await state.set_state(StepsForm.GET_NUMBER_RFB)
    
async def get_number_str(message: Message, state: FSMContext):
    await message.answer(f'Количество необработанных фидбеков для просмотра:\r\n{message.text}\r\n', reply_markup=get_inline_keyboard_yes_no())
    await state.set_state(StepsForm.CHECK_NUMBER_RFB)
    await state.update_data(number=message.text)

async def check_number_str(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if (call.data.endswith('yes')):
       await call.message.answer(f'Отлично, Вы подтвердили количество необработанных фидбеков для просмотра')
       await validate_number_show_raw_feedbacks(call.message, state)
       await state.set_state(StepsForm.VALIDATE_NUMBER_RFB)
    if (call.data.endswith('no')):
        await call.message.answer("Введите повторно количество необработанных фидбеков")
        await state.set_state(StepsForm.GET_NUMBER_RFB)

async def validate_number_show_raw_feedbacks(message: Message, state: FSMContext):
    # функиця валидации типа
    await message.answer(f'провалидировали все норм или нет))')
    await state.set_state(StepsForm.SHOW_RAW_FEEDBACKS)
    await message.answer(f'Наши шедевро необработанные фидбеки')
    # функция, которая показывает фидбеки
    await state.clear()
