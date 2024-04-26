from aiogram.fsm.state import StatesGroup, State

class StepsForm(StatesGroup):
    GET_LAST_NAME = State()
    GET_AGE = State()
    GET_CATEGORY = State()
    GET_DESCRIPTION = State()
    GET_LINK = State()
    GET_NAME = State()
    GET_AUTHOR = State()