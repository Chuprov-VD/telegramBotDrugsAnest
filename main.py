import aiogram.dispatcher.storage
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import random
# from aiogram import F

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext

with open('Token.txt') as file:
    token = file.readline()

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# @dp.message_handler(commands=["start"])
# async def cmd_start(message: types.Message):
# await message.answer(text = f"Привет, {message.from_user.first_name}!")

class RandomStates(StatesGroup):
    wait_num1 = State()
    wait_fio_num = State()
    wait_drugs = State()


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer(text = f"Привет, {message.from_user.first_name}!")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    hello = ["Привет!"]
    buttons = ["Дай пять!", "Дать пинка!"]
    comandas = ["Запустить рандом!", "Добавить пациента"]
    keyboard.add(*hello)
    keyboard.add(*buttons)
    keyboard.add(*comandas)
    await message.answer("Как будешь здороваться?", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Дай пять!")
async def with_puree(message: Message):
    await message.reply("Отличный выбор! Лови пять!")


@dp.message_handler(lambda message: message.text == "Дать пинка!")
async def without_puree(message: Message):
    await message.reply("Сам дурак!")


@dp.message_handler(lambda message: message.text == "Запустить рандом!")
async def cmd_random(message: Message):
    await message.answer(text="Введите № последнего билета: ")
    await RandomStates.wait_num1.set()

@dp.message_handler(state=RandomStates.wait_num1)
async def get_num1(message: Message, state: FSMContext):
    try:
        message.text = int(message.text)
    except ValueError:
        if type(message.text) != int:
            await message.answer(text="Введен текст, автоматически исправили на случайное число от 1 до 1000: ")
            message.text = random.randint(1, 1000)
    a = 1
    b = int(message.text)
    x = 4
    y = random.randint(a, b)
    await message.answer(text="Счет! ")
    while x > 0:
        x = x - 1
        y = random.randint(a, b)
        print(x, y)
        await message.answer(f"{x} - {y}")
    await message.answer(f"Выйгравший билет {y}, Поздравляем!")
    await state.reset_state()

@dp.message_handler(lambda message: message.text == "Добавить пациента")
async def cmd_patient(message: Message):
    await message.answer(text="Введите фамилию, и инициалы пациента, и номер истории")
    await RandomStates.wait_fio_num.set()

@dp.message_handler(state=RandomStates.wait_fio_num)
async def get_patient_num(message: Message, state: FSMContext):
    x = len(message.text) * "-"
    with open('history.txt', "a") as file:
        file.write(f"{x}\n{message.text}\n")
    await message.answer(text="Введите наименования и количество наркотиков")
    await RandomStates.wait_drugs.set()

@dp.message_handler(state=RandomStates.wait_drugs)
async def get_patient_num(message: Message, state: FSMContext):
    with open('history.txt', "a") as file:
        file.write(f"{message.text}\n - {message.from_user.first_name}")
        await message.answer(text="Спасибо, данные сохранены на сервере")
    await state.reset_state()
#   keyboard = types.InlineKeyboardMarkup()
#  keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
# await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 100", reply_markup=keyboard)


# @dp.message(F.text.lower() == "дать пять")
# async def with_five(message: types.Message):
#    await message.reply("Отличный выбор, лови пять!")

# @dp.message(F.text.lower() == "дать пинка")
# async def without_pinka(message: types.Message):
#    await message.reply("Сам получи пинка")

@dp.message_handler(text="Привет!")
async def hello_func(message: Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}!")


executor.start_polling(dispatcher=dp)

