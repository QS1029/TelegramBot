from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_start1():
    keyboard_main = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Как начать работать с гит в проекте?", callback_data = "push_tutorial")
    button1 = InlineKeyboardButton("Не могу сделать push в указанную ветку, почему?", callback_data = "push_issue")
    button2 = InlineKeyboardButton("Как отобразить свое имя в коммитах?", callback_data="commit_name_display")
    button3 = InlineKeyboardButton("[Стр. 2 - ]", callback_data = "go_to_2")
    keyboard_main.add(button, button1, button2, button3)
    return keyboard_main

def get_keyboard_start2():
    keyboard_main2 = InlineKeyboardMarkup(row_width=1)
    button3 = InlineKeyboardButton("Go to menu 1", callback_data = "go_to_1")
    button4 = InlineKeyboardButton("What time is it (im deranged i cant look it up myself)", callback_data="send_datetime")
    keyboard_main2.add(button3, button4)
    return keyboard_main2
