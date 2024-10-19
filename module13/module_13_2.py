from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Функция, которая обрабатывает команду /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print("Привет! Я бот помогающий твоему здоровью.")  # Сообщение в консоль

# Функция, которая обрабатывает любые другие сообщения
@dp.message_handler()
async def all_messages(message: types.Message):
    print("Введите команду /start, чтобы начать общение.")  # Сообщение в консоль

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
