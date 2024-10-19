from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = "7926186391:AAFqtGKdEmNINe7BK-QX5WS3h1hyft5flBI"  # Замените на свой токен API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Создаем основную клавиатуру
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')  # Кнопка информации
button_buy = KeyboardButton('Купить')  # Новая кнопка 'Купить'
keyboard.add(button_calculate, button_info, button_buy)  # Добавляем кнопку в клавиатуру

# Создаем inline-клавиатуру
inline_keyboard = InlineKeyboardMarkup()
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

# Данные о продуктах с локальными изображениями
products = [
    {"name": "Product1", "description": "Описание 1", "price": 100, "image": "img/vitamin_C.jpg"},
    {"name": "Product2", "description": "Описание 2", "price": 200, "image": "img/mandarin.jpg"},
    {"name": "Product3", "description": "Описание 3", "price": 300, "image": "img/vitamin_A.jpg"},
    {"name": "Product4", "description": "Описание 4", "price": 400, "image": "img/hamburger.jpg"},
]

# Создаем инлайн-клавиатуру для покупки
product_inline_keyboard = InlineKeyboardMarkup()
button_product1 = InlineKeyboardButton('Product1', callback_data='product_buying')
button_product2 = InlineKeyboardButton('Product2', callback_data='product_buying')
button_product3 = InlineKeyboardButton('Product3', callback_data='product_buying')
button_product4 = InlineKeyboardButton('Product4', callback_data='product_buying')
product_inline_keyboard.add(button_product1, button_product2, button_product3, button_product4)

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
    for product in products:
        await message.answer(
            f'Название: {product["name"]} | Описание: {product["description"]} | Цена: {product["price"]} руб.')
        with open(product["image"], 'rb') as photo:  # Открываем локальный файл изображения
            await message.answer_photo(photo=photo)  # Отправляем фото продукции

    await message.answer("Выберите продукт для покупки:", reply_markup=product_inline_keyboard)

@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Вы успешно приобрели продукт!")
    await call.answer()

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula = "Формула Миффлина-Сан Жеора для женщин: \nBMR = 10 * вес + 6.25 * рост - 5 * возраст - 161"
    await bot.send_message(call.message.chat.id, formula)
    await call.answer()  # Закрываем callback

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await bot.send_message(call.message.chat.id, "Введите свой возраст:")
    await UserState.age.set()  # Устанавливаем состояние age
    await call.answer()  # Закрываем callback

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Сохраняем возраст
    await message.answer("Введите свой рост:")
    await UserState.growth.set()  # Устанавливаем состояние growth

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Сохраняем рост
    await message.answer("Введите свой вес:")
    await UserState.weight.set()  # Устанавливаем состояние weight

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Сохраняем вес
    data = await state.get_data()  # Получаем данные
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Применяем формулу Миффлина - Сан Жеора (для женщин)
    calories = 10 * weight + 6.25 * growth - 5 * age - 161  # Базальный уровень метаболизма для женщин

    await message.answer(f"Ваша норма калорий: {calories} ккал.")
    await state.finish()  # Завершаем состояние

@dp.message_handler(text='Информация')  # Обработчик для кнопки 'Информация'
async def send_info(message: types.Message):
    await message.answer("Это бот для твоего здоровья.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
