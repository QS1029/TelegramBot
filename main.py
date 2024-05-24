from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards import get_keyboard_start1, get_keyboard_start2
from database.database import initialize_db, get_user, add_user

bot = Bot(token = TELEGRAM_TOKEN)
dp = Dispatcher(bot)
initialize_db()

#COMMAND LIST
async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command = '/start', description = "Вызвать меню"),
        types.BotCommand(command = '/help', description = "Памятка о библиотеке Телеграм бота"),
    ]
    await bot.set_my_commands(commands)

#START MENU
@dp.message_handler(commands = 'start')
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None: add_user(message.from_user.id, message.from_user.username, message.from_user.first_name,
    message.from_user.last_name)
    await message.answer('Ты можешь спросить меня о коммандах git, которые часто используются пользователями,'
                         'и часто забываются новичками. (Конкретно тобой :) )',
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

@dp.callback_query_handler(lambda c: c.data == 'token_question')
async def commit_name_display(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Если в вашем коде есть токены, их нужно грамотно скрыть перед push'ом на GitHub.\n"
                                        "1) Создайте файл .env в директории проекта, и напишите туда ваш токен\n"
                                        "   API_KEY = Ваш API ключ\n"
                                        "2) Создайте файл .py (можно назвать config.py), и напишите туда данный код:\n"
                                        "   import os\n"
                                        "   from dotenv import load_dotenv\n"
                                        "   load_dotenv()\n"
                                        "   ИмяПеременнойТокена = os.getenv('API_KEY')\n"
                                        "3) В вашем файле main.py импортируйте переменную с токеном из файла c кодом из 2 шага\n"
                                        "   from config.py import ИмяПеременнойТокена\n"
                                        "4) Создайте файл .gitignore, и впишите туда весь код с данной ссылки\n"
                                        "   https://www.toptal.com/developers/gitignore/api/python,venv")

@dp.callback_query_handler(lambda c: c.data == 'github_link')
async def commit_name_display(callback_query: types.CallbackQuery):
    await callback_query.message.answer("https://github.com/QS1029")

@dp.callback_query_handler(lambda c: c.data == 'practice_progress')
async def commit_name_display(callback_query: types.CallbackQuery):
    await callback_query.message.answer("За данную учебную практику было изучено несколько полезных тем:\n"
                                        "- Написание Telegram бота на языке Python\n"
                                        "- Использование разных клавиатур меню для бота Telegram\n"
                                        "- Написание и подключение к боту простой базы данных на SQL\n"
                                        "- Опыт в использовании GitHub и комманд Git\n"
                                        "- Написание нейро-ассистента в Telegram, с использованием YandexGPT")

@dp.callback_query_handler(lambda c: c.data == 'go_to_2')
async def go_to_2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты можешь спросить меня о коммандах git, которые часто используются пользователями,'
                         'и часто забываются новичками. (Конкретно тобой :) )',
                           reply_markup = get_keyboard_start2())

@dp.callback_query_handler(lambda c: c.data == 'go_to_1')
async def go_to_1(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты можешь спросить меня о коммандах git, которые часто используются пользователями,'
                         'и часто забываются новичками. (Конкретно тобой :) )', reply_markup=get_keyboard_start1())

#HELP
@dp.message_handler(commands = 'help')
async def help(message: types.Message):
    await message.answer('Бот написан с использованием aiogram 2.22.2')

#STANDART REPLY
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Я не способен разговаривать с тобой, нажми на кнопку в меню.')

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True, on_startup = on_startup)