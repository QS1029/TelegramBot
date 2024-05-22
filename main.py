from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_start1, get_keyboard_start2, get_keyboard_inline
from database.database import initialize_db, get_user, add_user
import random
from datetime import datetime

bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)
initialize_db()

#COMMAND LIST
async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command = '/start', description = "star anew"),
        types.BotCommand(command = '/help', description = "ask for assistance"),
        types.BotCommand(command = '/lobotomy', description = "but would you win?")
    ]
    await bot.set_my_commands(commands)

#START MENU
@dp.message_handler(commands = 'start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None: add_user(message.from_user.id, message.from_user.username, message.from_user.first_name,
    message.from_user.last_name)
    await message.reply('hiiiiii welcome the main menu of this definetely good bot!!!',
                        reply_markup = get_keyboard_start1())

@dp.callback_query_handler(lambda c: c.data == 'send_random_number')
async def random_number(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"uhhhh, here you can have this {random.randint(1,100)}")

@dp.callback_query_handler(lambda c: c.data == 'send_datetime')
async def send_datetime(callback_query: types.CallbackQuery):
    await callback_query.message.answer(f"its currenntly {datetime.now().strftime('%H:%M:%S')}")

@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Sentenced to be sealed away in keyboard 2 (Unseal yourself with that button fr)',
                           reply_markup = get_keyboard_start2())

@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_1(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Sentenced to be sealed away in keyboard 1 (Unseal yourself with that button fr)',
                            reply_markup=get_keyboard_start1())

#HELP
@dp.message_handler(commands = 'help')
async def help(message: types.Message):
    await message.reply('how about you kindly discombobulat e')

#LOBOTOMY
@dp.message_handler(commands='lobotomy')
async def help(message: types.Message):
    await message.answer('am i the worst telegram bot because i was made by you, or was i made by you because i am the worst telegram bot?')

#STANDART REPLY
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('a very thoughtful reply, hmmm yes yes i agree')

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True, on_startup = on_startup)