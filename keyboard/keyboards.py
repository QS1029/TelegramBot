from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard = True)
    button_1 = KeyboardButton('send me a kitty!11!11')
    button_2 = KeyboardButton('Would. Next keyboard.')
    keyboard.add(button_1, button_2)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard = True)
    button_3 = KeyboardButton('send me another kitty!!!11')
    button_4 = KeyboardButton('Would not. Previous keyboard.')
    button_5 = KeyboardButton('Maybe would. Next keyboard.')
    keyboard_2.add(button_3, button_4, button_5)
    return keyboard_2

def get_keyboard_3():
    keyboard_3 = ReplyKeyboardMarkup(resize_keyboard = True)
    button_6 = KeyboardButton('send me more critters...')
    button_7 = KeyboardButton('Def no. Previous keyboard.')
    keyboard_3.add(button_6, button_7)
    return keyboard_3