from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3  # Добавлен импорт sqlite3
import crud_functions  # Импортируем файл с функциями работы с БД

api = ""  # Замените на свой токен API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Создаем основную клавиатуру
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')
keyboard.add(button_calculate, button_info, button_buy)

# Создаем inline-клавиатуру для опций
inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

# Инициализируем базу данных и заполняем её данными
crud_functions.initiate_db()


# Пополняем таблицу данными (это следует выполнять один раз или в каждом запуске при отсутствии записей)
  # Заполняем базу данными


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Я бот, помогающий твоему здоровью.", reply_markup=keyboard)


@dp.message_handler(text='Привет!')
async def greet(message: types.Message):
    await message.answer("Привет! Введите команду /start, чтобы начать общение.")


@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)


@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    products = crud_functions.get_all_products()  # Получаем продукты из БД
    for title, description, price in products:
        await message.answer(
            f'Название: {title} | Описание: {description} | Цена: {price} руб.'
        )
        image_path = f'img/{title}.jpg'  # Убедитесь, что изображения имеют соответствующие названия
        try:
            with open(image_path, 'rb') as photo:
                await message.answer_photo(photo=photo)
        except FileNotFoundError:
            await message.answer("Изображение отсутствует.")  # На случай, если изображение не найдено

    await message.answer("Выберите продукт для покупки:", reply_markup=product_inline_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Вы успешно приобрели продукт!")
    await call.answer()


@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula = "Формула Миффлина-Сан Жеора для женщин: \nBMR = 10 * вес + 6.25 * рост - 5 * возраст - 161"
    await bot.send_message(call.message.chat.id, formula)
    await call.answer()


@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Ваша норма калорий: {calories} ккал.")
    await state.finish()


@dp.message_handler(text='Информация')
async def send_info(message: types.Message):
    await message.answer("Это бот для твоего здоровья.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
