from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_start1():
    keyboard_main = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Как начать работать с гит в проекте?", callback_data = "push_tutorial")
    button1 = InlineKeyboardButton("Не могу сделать push в указанную ветку, почему?", callback_data = "push_issue")
    button2 = InlineKeyboardButton("Как отобразить свое имя в коммитах?", callback_data="commit_name_display")
    button3 = InlineKeyboardButton("[Стр. 2]", callback_data = "go_to_2")
    keyboard_main.add(button, button1, button2, button3)
    return keyboard_main

def get_keyboard_start2():
    keyboard_main2 = InlineKeyboardMarkup(row_width=1)
    button4 = InlineKeyboardButton("Что мне нужно сделать, перед тем как push'нуть код, "
                                   "включающий в себя токены?", callback_data="token_question")
    button5 = InlineKeyboardButton("Список изученного за учебную практику", callback_data="practice_progress")
    button6 = InlineKeyboardButton("[Стр. 1]", callback_data = "go_to_1")
    keyboard_main2.add(button4, button5, button6)
    return keyboard_main2
