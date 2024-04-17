from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm


async def get_form(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, начинаем заполнять анкету. Введи сове имя')
    await state.set_state(StepsForm.GET_NAME)

async def get_name(message: Message, state: FSMContext):
    await message.answer(f'Твое имя:\r\n{message.text}\r\nТеперь введи фамилию')
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_LAST_NAME)

async def get_last_name(message: Message, state: FSMContext):
    await message.answer(f'Твоя фамилия:\r\n{message.text}\r\nТеперь ты дурак введи возраст')
    await state.update_data(last_name=message.text)
    await state.set_state(StepsForm.GET_AGE)

async def get_age(message: Message, state: FSMContext):
    await message.answer(f'Твой возраст:\r\n{message.text}\r\n')
    context_data = await state.get_data()
    await message.answer(f'Сохраненные данные в машине состояний:\r\n{str(context_data)}')
    name = context_data.get('name')
    last_name = context_data.get('last_name')
    data_user = f'Твои данные\r\n' \
    f'Имя{name}\r\n' \
    f'Имя{last_name}\r\n' \
    f'Возраст {message.text}'
    await message.answer(data_user)
    await state.clear()

