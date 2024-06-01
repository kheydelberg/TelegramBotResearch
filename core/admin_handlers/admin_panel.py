from aiogram.types import CallbackQuery
from core.utils.admin_statesform import StepsForm
from aiogram.fsm.context import FSMContext


async def admin_panel(call: CallbackQuery, state: FSMContext):
    await call.answer()
    if (call.data.endswith('help_admin')):
       await call.message.answer(f'помочь пока не могу')
    if (call.data.endswith('show_db')):
        await call.message.answer(f'Введите количество строк, которые хотите посмотреть')
        await state.set_state(StepsForm.GET_NUMBER_DB)
    if (call.data.endswith('add_material')):
        await call.message.answer(f'начинаем добавлять материал. Введи категорию материала')
        await state.set_state(StepsForm.GET_CATEGORY) 
    if (call.data.endswith('delete_material_id')):
        # функция, которая показывает базу данных
        await call.message.answer(f'начинаем удалять материал. Введите id материала, который хотите удалить')
        await state.set_state(StepsForm.GET_ID)
    if (call.data.endswith('show_feedbacks')):
        await call.message.answer(f'Введите количество фидбеков, которые хотите посмотреть')
        await state.set_state(StepsForm.GET_NUMBER_FB)
    if (call.data.endswith('show_raw_feedbacks')):
        await call.message.answer(f'Введите количество необработанных фидбеков, которые хотите посмотреть')
        await state.set_state(StepsForm.GET_NUMBER_RFB)
    if (call.data.endswith('changing_feedback_status')):
        # функция, которая показывает необр фидбеки или обр фидбеки?
        await call.message.answer(f'начинаем изменение статуса фидбека. Введите id фидбека')
        await state.set_state(StepsForm.GET_ID_FB)
    if (call.data.endswith('show_statistic')):
        await call.message.answer(f'Введите количество строк, которые хотите посмотреть')
        await state.set_state(StepsForm.GET_NUMBER_ST)
    if (call.data.endswith('make_backup')):
        # функция, которая делает бэкап, подробностей пока нет))
        await call.message.answer(f'Бэкап тип сделан') 
    if (call.data.endswith('load_backup')):
       # функция, которая загружает бэкап, подробностей пока нет))
       await call.message.answer(f'Бэкап тип загружен')
        
    