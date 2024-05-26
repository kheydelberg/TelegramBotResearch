# Модуль, содержащий глобальные переменные и функции для их изменения
current_page = 1
books_per_page = 3

def get_current_page():
    global current_page
    return current_page

def get_books_per_page():
    global books_per_page
    return books_per_page

# def set_current_page(value):
#     global current_page
#     current_page = value

def increment_current_page():
    global current_page
    current_page += 1

def decrement_current_page():
    global current_page
    current_page -= 1
