from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.keyboards.inline_keyboard import get_inline_keyboard
from core.utils.statesform import StepsForm
from aiogram.types import Message, CallbackQuery



async def show_db_to_delete(message: Message, state: FSMContext):
    # функция, которая показывает базу данных
    await message.answer(f'{message.from_user.first_name}, начинаем удалять материал. Введите id материала, который хотите удалить')
    await state.set_state(StepsForm.GET_ID)
    
async def get_id(message: Message, state: FSMContext):
    await message.answer(f'ID:\r\n{message.text}\r\n', reply_markup=get_inline_keyboard())
    await state.set_state(StepsForm.CHECK_ID)
    await state.update_data(id=message.text)

async def check_id(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if (call.data.endswith('yes')):
       await call.message.answer(f'Отлично, Вы подтвердили ID')
       await state.set_state(StepsForm.VALIDATE_ID)
       await validate_id_delete_material(call.message, state)

    if (call.data.endswith('no')):
        await call.message.answer("Введите повторно ID")
        await state.set_state(StepsForm.GET_ID)

async def validate_id_delete_material(message: Message, state: FSMContext):
    # функиця валидации типа
    await message.answer(f'провалидировали все норм или нет)))')
    await state.set_state(StepsForm.SHOW_STATISTIC)
    # функция, которая удаляет материал
    await message.answer(f'Обучающий материал был удален')
    await state.clear()
    