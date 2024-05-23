from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_start1, get_keyboard_start2
from database.database import initialize_db, get_user, add_user
import random
from datetime import datetime

bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)
initialize_db()

#COMMAND LIST
async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command = '/start', description = "Вызвать меню"),
        types.BotCommand(command = '/help', description = "Памятка о библиотеке Телеграм бота"),
        #types.BotCommand(command = '/lobotomy', description = "but would you win?")
    ]
    await bot.set_my_commands(commands)

#START MENU
@dp.message_handler(commands = 'start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None: add_user(message.from_user.id, message.from_user.username, message.from_user.first_name,
    message.from_user.last_name)
    await message.answer('Ты можешь спросить меня о коммандах git, которые часто используются пользователями,'
                         'и часто забываются новичками.',
                        reply_markup = get_keyboard_start1())

@dp.callback_query_handler(lambda c: c.data == 'push_tutorial')
async def push_tutorial(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Зайдите в терминал и введите данные команды:\n"
                                        "1) git init (Инициализирует работу гит)\n"
                                        "2) git add . (Выбирает все измененные файлы)\n"
                                        "3) git commit -m 'Напишите сюда последние изменения'\n"
                                        "4) git remote add названиеРемоута 'ссылка на репозиторий'\n"
                                        "5) git push -u названиеРемоута имяВетки")

@dp.callback_query_handler(lambda c: c.data == 'push_issue')
async def push_issue(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Вероятно ты создал ветку через сайт, а не через терминал.\n"
                                           "Удали ветку на GitHub, и напиши данную команду в терминал:\n"
                                           "git branch имяВетки (Cоздает ветку под указанным именем.")

@dp.callback_query_handler(lambda c: c.data == 'commit_name_display')
async def commit_name_display(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Нужно ввести пару простых комманд, и если понадобится, указать в них нужные вам значения.\n"
                                           "git config --global 'user.name' 'Введите сюда свое имя, "
                                           "оставить пустым для отображения имени вашего компьютера.\n"
                                           "git config --global 'user.email' 'Введите сюда ваш EMail.'")

@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Sentenced to be sealed away in keyboard 2 (Unseal yourself with that button fr)',
                           reply_markup = get_keyboard_start2())

@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_1(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты можешь спросить меня о коммандах git, которые часто используются пользователями,'
                         'и часто забываются новичками.', reply_markup=get_keyboard_start1())

#HELP
@dp.message_handler(commands = 'help')
async def help(message: types.Message):
    await message.answer('При написании нового бота, устанавливай aiogram версии 2.22.2')

#LOBOTOMY
@dp.message_handler(commands='lobotomy ')
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