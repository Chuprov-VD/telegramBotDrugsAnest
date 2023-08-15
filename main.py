from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor


with open('Token.txt') as file:
    token = file.readline()
bot = Bot(token)
db = Dispatcher(bot)

@db.message_handler(text = "Привет")
async def hello_func(message: Message):
    await message.answer(text = f"Привет, {message.from_user.first_name}!")

executor.start_polling(dispatcher = db)

