from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_start1():
    keyboard_main = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton("Go to menu 2", callback_data = "go_to_2")
    button2 = InlineKeyboardButton("Send me a random number (If I roll a 6 you fucking die)", callback_data="send_random_number")
    keyboard_main.add(button1, button2)
    return keyboard_main

def get_keyboard_start2():
    keyboard_main2 = InlineKeyboardMarkup(row_width=1)
    button3 = InlineKeyboardButton("Go to menu 1", callback_data = "go_to_1")
    button4 = InlineKeyboardButton("What time is it (im deranged i cant look it up myself)", callback_data="send_datetime")
    keyboard_main2.add(button3, button4)
    return keyboard_main2

def get_keyboard_inline(): #for the first keyboard
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton("Посмотреть", url="https://i.ytimg.com/vi/QlChyW_6kYA/maxresdefault.jpg")
    but_inline_2 = InlineKeyboardButton("Что-то", url="https://patents.google.com/patent/US20090292143A1/en")
    keyboard_inline.add(but_inline, but_inline_2)
    return keyboard_inline