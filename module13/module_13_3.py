from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Функция, которая обрабатывает команду /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")  # Отправляем сообщение в чат

# Функция, которая обрабатывает любые другие сообщения
@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")  # Отправляем сообщение в чат

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
