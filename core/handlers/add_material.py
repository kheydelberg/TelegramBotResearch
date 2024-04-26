from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm


async def get_material(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, начинаем добавлять материал. Введи категорию материала')
    await state.set_state(StepsForm.GET_CATEGORY)
    

async def get_category(message: Message, state: FSMContext):
    await message.answer(f'Категория материала:\r\n{message.text}\r\nДалее напиши короткое описание материала')
    await state.update_data(category=message.text)
    await state.set_state(StepsForm.GET_DESCRIPTION)

async def get_description(message: Message, state: FSMContext):
    await message.answer(f'Короткое описание материала:\r\n{message.text}\r\nДалее введи ссылку на материал')
    await state.update_data(description=message.text)
    await state.set_state(StepsForm.GET_LINK)

async def get_link(message: Message, state: FSMContext):
    await message.answer(f'Ссылка на материал:\r\n{message.text}\r\nДалее введи название материала')
    await state.update_data(link=message.text)
    await state.set_state(StepsForm.GET_NAME)

async def get_name(message: Message, state: FSMContext):
    await message.answer(f'Название материала:\r\n{message.text}\r\nДалее введи автора материала')
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_AUTHOR)

async def get_author(message: Message, state: FSMContext):
    await message.answer(f'Автор материала:\r\n{message.text}\r\n')
    await state.update_data(author=message.text)
    context_data = await state.get_data()
    await message.answer(f'Сохраненные данные в машине состояний:\r\n{str(context_data)}')
    category = context_data.get('category')
    description = context_data.get('description')
    link = context_data.get('link')
    name = context_data.get('name')
    author = context_data.get('author')
    data_user = f'Введенные данные\r\n' \
    f'Категория {category}\r\n' \
    f'Описание {description}\r\n' \
    f'Ссылка {link}\r\n' \
    f'Название {name}\r\n' \
    f'Атвор {author}'
    await message.answer(data_user)
    await state.clear()