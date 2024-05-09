from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.keyboards.admin_inline_keyboard import get_inline_keyboard
from core.utils.admin_statesform import StepsForm
from aiogram.types import Message, CallbackQuery


async def show_fb_to_changing_fb_status(message: Message, state: FSMContext):
    # функция, которая показывает необр фидбеки или обр фидбеки?
    await message.answer(f'{message.from_user.first_name}, начинаем изменение статуса фидбека. Введите id фидбека')
    await state.set_state(StepsForm.GET_ID_FB)
    
async def get_id_fb(message: Message, state: FSMContext):
    await message.answer(f'ID:\r\n{message.text}\r\n', reply_markup=get_inline_keyboard())
    await state.set_state(StepsForm.CHECK_ID_FB)
    await state.update_data(id=message.text)

async def check_id_fb(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if (call.data.endswith('yes')):
       await call.message.answer(f'Отлично, Вы подтвердили ID')
       await state.set_state(StepsForm.VALIDATE_ID_FB)
       await validate_id_change_status(call.message, state)

    if (call.data.endswith('no')):
        await call.message.answer("Введите повторно ID")
        await state.set_state(StepsForm.GET_ID_FB)

async def validate_id_change_status(message: Message, state: FSMContext):
    # функиця валидации типа
    await message.answer(f'провалидировали все норм или нет)))')
    await state.set_state(StepsForm.CHANGE_STATUS_FB)
    # функция, которая меняет статус у фидбека
    await message.answer(f'Поменяли статус тип')
    await state.clear()
    