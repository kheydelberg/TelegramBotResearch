from aiogram.fsm.state import StatesGroup, State

class StepsForm(StatesGroup):
   
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
    ADD_MATERIAL = State()
    GET_FORMAT = State()

    DELETE_MATERIAL = State()
    GET_ID = State()
    CHECK_ID = State()
    VALIDATE_ID = State()

    GET_NUMBER_DB = State()
    CHECK_NUMBER_DB = State()
    VALIDATE_NUMBER_DB = State()
    SHOW_DB = State()

    GET_NUMBER_FB = State()
    CHECK_NUMBER_FB = State()
    VALIDATE_NUMBER_FB = State()
    SHOW_FEEDBACKS = State()

    GET_NUMBER_RFB = State()
    CHECK_NUMBER_RFB = State()
    VALIDATE_NUMBER_RFB = State()
    SHOW_RAW_FEEDBACKS = State()

    GET_NUMBER_ST = State()
    CHECK_NUMBER_ST = State()
    VALIDATE_NUMBER_ST = State()
    SHOW_STATISTIC = State()

    GET_ID_FB = State()
    CHECK_ID_FB = State()
    VALIDATE_ID_FB = State()
    CHANGE_STATUS_FB = State()

    EXTRACT = State()