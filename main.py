from aiogram import Bot, Dispatcher,types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_1, get_keyboard_2, get_keyboard_3

bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)

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
    await message.reply('hiiiiii welcome the main menu of this definetely good bot!!!',
                        reply_markup = get_keyboard_1())


#STUFF BELOW THIS LINE ISNT BEING USED NOW (ILL KEEP IT ANYWAY)

#KEYBOARD1
#-----------------------------------------

#KITTY PIC
@dp.message_handler(lambda message: message.text == "send me a kitty!11!11")
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo = 'https://i.pinimg.com/originals/a4/24/ab/a424ab7e7e419a35a4f980eb5ed84921.jpg',
                         caption = 'he is wanted in 15 countires across the world.')

#PROCEED TO KEYBOARD2
@dp.message_handler(lambda message: message.text == "Would. Next keyboard.")
async def button_2_click(message: types.Message):
    await message.answer("THE PUNCHLINE IS- Let us proceed to the next keyboard, fine gentleman.", reply_markup = get_keyboard_2())
#-----------------------------------------

#KEYBOARD2
#-----------------------------------------

#ANOTHER KITTY PIC
@dp.message_handler(lambda message: message.text == "send me another kitty!!!11")
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo = 'https://i.pinimg.com/originals/57/c3/e6/57c3e6125d790ea5db39c8b79c861414.jpg', caption = 'he commited 72 different crimes and isnt planning on stopping')
#PROCEED TO KEYBOARD1
@dp.message_handler(lambda message: message.text == "Would not. Previous keyboard.")
async def button_4_click(message: types.Message):
    await message.answer("ok yes i understand hmmm yes yes keyboard 1", reply_markup = get_keyboard_1())

#PROCEED TO KEYBOARD3
@dp.message_handler(lambda message: message.text == "Maybe would. Next keyboard.")
async def button_5_click(message: types.Message):
    await message.answer("ah i see a most excellent choice, keyboard 3 yes yes", reply_markup = get_keyboard_3())
#-----------------------------------------

#KEYBOARD3
#-----------------------------------------

#YET ANOTHER KITTY PIC (its never enough)
@dp.message_handler(lambda message: message.text == "send me more critters...")
async def button_6_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo = 'https://i.ytimg.com/vi/QlChyW_6kYA/maxresdefault.jpg', caption = 'bro is so silly he got into the silly competition')

#PROCEED TO KEYBOARD2
@dp.message_handler(lambda message: message.text == "Def no. Previous keyboard.")
async def button_5_click(message: types.Message):
    await message.answer("understandable, returning to keyboard 2 hq", reply_markup = get_keyboard_2())
#-----------------------------------------

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