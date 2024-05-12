from core.handlers.basic import get_help
from core.keyboards.reply import create_pagination_keyboard, do_you_like, get_Math_Prog, get_category_of_math, get_category_of_prog
from aiogram.types import InlineKeyboardMarkup
import pytest


def test_get_Math_Prog():
    # Получаем результат вызова функции
    result = get_Math_Prog()

    # Проверяем, что результат не равен None
    assert result is not None

    # Проверяем, что результат является объектом InlineKeyboardMarkup
    assert isinstance(result, InlineKeyboardMarkup)

    # Проверяем, что количество строк равно 1
    assert len(result.inline_keyboard) == 1

    # Проверяем, что количество кнопок равно 2
    assert len(result.inline_keyboard[0]) == 2

    # Проверяем текст кнопок и их коллбэк-данные
    assert result.inline_keyboard[0][0].text == 'Высшая математика'
    assert result.inline_keyboard[0][0].callback_data == 'math'
    assert result.inline_keyboard[0][1].text == 'Программирование'
    assert result.inline_keyboard[0][1].callback_data == 'prog'

    print("get_Math_Prog passed the test")


def test_get_category_of_math():
    # Получаем результат вызова функции
    result = get_category_of_math()

    # Проверяем, что результат не равен None
    assert result is not None

    # Проверяем, что результат является объектом InlineKeyboardMarkup
    assert isinstance(result, InlineKeyboardMarkup)

    # Проверяем, что количество строк равно 1
    assert len(result.inline_keyboard) == 7

    # Проверяем, что количество кнопок равно 7
    assert len(result.inline_keyboard[0]) == 1
    assert len(result.inline_keyboard[1]) == 1
    assert len(result.inline_keyboard[2]) == 1
    assert len(result.inline_keyboard[3]) == 1
    assert len(result.inline_keyboard[4]) == 1
    assert len(result.inline_keyboard[5]) == 1
    assert len(result.inline_keyboard[6]) == 1


    # Проверяем текст кнопок и их коллбэк-данные
    assert result.inline_keyboard[0][0].text == 'Математический анализ'
    assert result.inline_keyboard[0][0].callback_data == 'matan'
    assert result.inline_keyboard[1][0].text == 'Линейная алгебра'
    assert result.inline_keyboard[1][0].callback_data == 'linal'
    assert result.inline_keyboard[2][0].text == 'Дискретная математика'
    assert result.inline_keyboard[2][0].callback_data == 'discra'
    assert result.inline_keyboard[3][0].text == 'Геометрия и топология'
    assert result.inline_keyboard[3][0].callback_data == 'git'
    assert result.inline_keyboard[4][0].text == 'Дифференциальные уравнения'
    assert result.inline_keyboard[4][0].callback_data == 'diffur'
    assert result.inline_keyboard[5][0].text == 'Теория вероятности и мат. статистика'
    assert result.inline_keyboard[5][0].callback_data == 'twims'
    assert result.inline_keyboard[6][0].text == 'Назад'
    assert result.inline_keyboard[6][0].callback_data == 'back_math'

    print("get_category_of_math passed the test")


def test_get_category_of_prog():
    # Получаем результат вызова функции
    result = get_category_of_prog()

    # Проверяем, что результат не равен None
    assert result is not None

    # Проверяем, что результат является объектом InlineKeyboardMarkup
    assert isinstance(result, InlineKeyboardMarkup)

    # Проверяем, что количество строк равно 2
    assert len(result.inline_keyboard) == 3

    # Проверяем, что количество кнопок в каждой строке равно 2
    assert len(result.inline_keyboard[0]) == 2
    assert len(result.inline_keyboard[1]) == 2
    assert len(result.inline_keyboard[2]) == 1

    # Проверяем текст кнопок и их коллбэк-данные
    assert result.inline_keyboard[0][0].text == 'C++'
    assert result.inline_keyboard[0][0].callback_data == 'C++'
    assert result.inline_keyboard[0][1].text == 'C#'
    assert result.inline_keyboard[0][1].callback_data == 'C#'
    assert result.inline_keyboard[1][0].text == 'Python'
    assert result.inline_keyboard[1][0].callback_data == 'python'
    assert result.inline_keyboard[1][1].text == 'Java'
    assert result.inline_keyboard[1][1].callback_data == 'java'
    assert result.inline_keyboard[2][0].text == 'Назад'
    assert result.inline_keyboard[2][0].callback_data == 'back_prog'

    print("get_category_of_prog passed the test")



def test_create_pagination_keyboard():
    # Получаем результат вызова функции
    result = create_pagination_keyboard("prev", "1", "2", "3", "next")

    # Проверяем, что результат не равен None
    assert result is not None

    # Проверяем, что результат является объектом InlineKeyboardMarkup
    assert isinstance(result, InlineKeyboardMarkup)

    # Проверяем количество строк клавиатуры
    assert len(result.inline_keyboard) == 1

    # Проверяем количество кнопок в строке
    assert len(result.inline_keyboard[0]) == 5

    # Проверяем текст кнопок и их коллбэк-данные
    assert result.inline_keyboard[0][0].text == 'prev'
    assert result.inline_keyboard[0][0].callback_data == 'prev'
    assert result.inline_keyboard[0][1].text == '1'
    assert result.inline_keyboard[0][1].callback_data == '1'
    assert result.inline_keyboard[0][2].text == '2'
    assert result.inline_keyboard[0][2].callback_data == '2'
    assert result.inline_keyboard[0][3].text == '3'
    assert result.inline_keyboard[0][3].callback_data == '3'
    assert result.inline_keyboard[0][4].text == 'next'
    assert result.inline_keyboard[0][4].callback_data == 'next'

    print("create_pagination_keyboard passed the test")



def test_do_you_like():
    # Получаем результат вызова функции
    result = do_you_like()

    # Проверяем, что результат не равен None
    assert result is not None

    # Проверяем, что результат является объектом InlineKeyboardMarkup
    assert isinstance(result, InlineKeyboardMarkup)

    # Проверяем количество строк клавиатуры
    assert len(result.inline_keyboard) == 1

    # Проверяем количество кнопок в строке
    assert len(result.inline_keyboard[0]) == 2

    # Проверяем текст кнопок и их коллбэк-данные
    assert result.inline_keyboard[0][0].text == 'Да👌'
    assert result.inline_keyboard[0][0].callback_data == 'like'
    assert result.inline_keyboard[0][1].text == 'Нет😒'
    assert result.inline_keyboard[0][1].callback_data == 'not_like'

    print("do_you_like passed the test")


test_get_Math_Prog()
test_get_category_of_math()
test_get_category_of_prog()
test_create_pagination_keyboard()
test_create_pagination_keyboard()
test_do_you_like()
