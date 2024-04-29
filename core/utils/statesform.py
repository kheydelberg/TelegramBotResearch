from aiogram.fsm.state import StatesGroup, State

class StepsForm(StatesGroup):
    """
    GET_LAST_NAME = State()
    GET_AGE = State()
    """

    GET_CATEGORY = State()
    CHECK_CATEGORY = State()
    
    GET_DESCRIPTION = State()
    CHECK_DESCRIPTION = State()
   
    GET_LINK = State()
    CHECK_LINK = State()
   
    GET_NAME = State()
    CHECK_NAME = State()
   
    GET_AUTHOR = State()
    CHECK_AUTHOR = State()

    GET_ALL = State()

    VALIDATE_MATERIAL = State()