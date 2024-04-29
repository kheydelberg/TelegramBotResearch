from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.keyboards.inline_keyboard import get_inline_keyboard
from core.utils.statesform import StepsForm
from aiogram.types import Message, CallbackQuery


async def get_material(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, начинаем добавлять материал. Введи категорию материала')
    await state.set_state(StepsForm.GET_CATEGORY)
    
async def get_category(message: Message, state: FSMContext):
    await message.answer(f'Категория материала:\r\n{message.text}\r\n', reply_markup=get_inline_keyboard())
    await state.set_state(StepsForm.CHECK_CATEGORY)
    await state.update_data(category=message.text)

async def check_category(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if (call.data.endswith('yes')):
       await call.message.answer("Отлично, Вы подтвердили категорию. Введи еще")
       await state.set_state(StepsForm.GET_DESCRIPTION)
    if (call.data.endswith('no')):
        await call.message.answer("Введите повторно категорию")
        await state.set_state(StepsForm.GET_CATEGORY)

async def get_description(message: Message, state: FSMContext):
    await message.answer(f'Короткое описание материала:\r\n{message.text}\r\n', reply_markup=get_inline_keyboard())
    await state.set_state(StepsForm.CHECK_DESCRIPTION)
    await state.update_data(description=message.text)

async def check_description(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if (call.data.endswith('yes')):
       await call.message.answer("Отлично, Вы подтвердили. Введи еще")
       await state.set_state(StepsForm.GET_LINK)
    if (call.data.endswith('no')):
        await call.message.answer("Введите повторно")
        await state.set_state(StepsForm.GET_DESCRIPTION)

async def get_link(message: Message, state: FSMContext):
    await message.answer(f'Ссылка на материал:\r\n{message.text}\r\n', reply_markup=get_inline_keyboard())
    await state.set_state(StepsForm.CHECK_LINK)
    await state.update_data(link=message.text)

async def check_link(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if (call.data.endswith('yes')):
       await call.message.answer("Отлично, Вы подтвердили. Введи еще")
       await state.set_state(StepsForm.GET_NAME)
    if (call.data.endswith('no')):
        await call.message.answer("Введите повторно")
        await state.set_state(StepsForm.GET_LINK)    

async def get_name(message: Message, state: FSMContext):
    await message.answer(f'Название материала:\r\n{message.text}\r\n', reply_markup=get_inline_keyboard())
    await state.set_state(StepsForm.CHECK_NAME)
    await state.update_data(name=message.text)

async def check_name(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if (call.data.endswith('yes')):
       await call.message.answer("Отлично, Вы подтвердили. Введи еще")
       await state.set_state(StepsForm.GET_AUTHOR)
    if (call.data.endswith('no')):
        await call.message.answer("Введите повторно")
        await state.set_state(StepsForm.GET_NAME)  

async def get_author(message: Message, state: FSMContext):
    await message.answer(f'Автор материала:\r\n{message.text}\r\n',reply_markup=get_inline_keyboard())
    await state.set_state(StepsForm.CHECK_AUTHOR)
    await state.update_data(author=message.text)

async def check_author(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if (call.data.endswith('yes')):
       await call.message.answer("Отлично, Вы подтвердили")
       await state.set_state(StepsForm.GET_ALL)
    if (call.data.endswith('no')):
        await call.message.answer("Введите повторно")
        await state.set_state(StepsForm.GET_AUTHOR)  

async def get_all(message: Message, state: FSMContext):
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
    await message.answer('Данные отправлены на валидацию')
    await state.set_state(StepsForm.VALIDATE_MATERIAL)
    await message.answer(data_user)
    #await state.clear()

async def validate_material(message: Message, state: FSMContext):
    # функция Жени
    await state.clear()
    await message.answer('лол провалидировали типо')

    
