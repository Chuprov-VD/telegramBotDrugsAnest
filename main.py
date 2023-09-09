from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import random
# from aiogram import F
from aiogram.dispatcher.filters import Text



with open('Token.txt') as file:
    token = file.readline()
bot = Bot(token)
db = Dispatcher(bot)

# @db.message_handler(commands=["start"])
# async def cmd_start(message: types.Message):
    # await message.answer(text = f"Привет, {message.from_user.first_name}!")

@db.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Дай пять!", "Дать пинка!"]
    comandas = ["/random"]
    keyboard.add(*buttons)
    keyboard.add(*comandas)
    await message.answer("Как будешь здороваться?", reply_markup=keyboard)
@db.message_handler(Text(equals="Дай пять!"))
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор! Лови пять!")


@db.message_handler(lambda message: message.text == "Дать пинка!")
async def without_puree(message: types.Message):
    await message.reply("Сам дурак!")
@db.message_handler(commands="random")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 100", reply_markup=keyboard)
@db.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    a = random.randint(1, 23)
    b = random.randint(1, 23)
    while a != b:
        a = random.randint(1, 23)
        b = random.randint(1, 23)
        print(a, b)
        await call.message.answer(f"{a}, {b}")
    await call.message.answer(f"Выйгравший билет {a}, Поздравляем!")

#@db.message(F.text.lower() == "дать пять")
# async def with_five(message: types.Message):
#    await message.reply("Отличный выбор, лови пять!")

# @db.message(F.text.lower() == "дать пинка")
# async def without_pinka(message: types.Message):
#    await message.reply("Сам получи пинка")

@db.message_handler(text = "Привет")
async def hello_func(message: Message):
    await message.answer(text = f"Привет, {message.from_user.first_name}!")

executor.start_polling(dispatcher = db)

