from aiogram.fsm.state import StatesGroup, State

class UserState(StatesGroup):
    PICK_LINK = State()
    NOT_PICK_LINK = State()
    GET_GPT_REQUEST = State()