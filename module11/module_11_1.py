import requests
import pandas as pd
import matplotlib.pyplot as plt

# 1. Использование requests для получения данных
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()

# Преобразуем данные в DataFrame с pandas
df = pd.DataFrame(data)

# Выводим первые 5 записей DataFrame
print("Первые 5 записей:")
print(df.head())

# 2. Анализ данных с использованием pandas
# Например, подсчёт количества постов по пользователю
post_counts = df['userId'].value_counts()
print("\nКоличество постов по пользователю:")
print(post_counts)

# 3. Визуализация данных с помощью matplotlib
# Печатаем график количества постов по пользователям
plt.bar(post_counts.index, post_counts.values)
plt.title('Количество постов по пользователям')
plt.xlabel('ID пользователя')
plt.ylabel('Количество постов')
plt.xticks(post_counts.index)  # Указываем метки для оси X
plt.show()

# Возможности requests:
# - Работа с HTTP-запросами (GET, POST и т.д.)
# - Поддержка параметров и заголовков.
# - Удобная работа с JSON-данными.

# Возможности pandas:
# - Мощные структуры данных (DataFrame и Series)
# - Анализ данных (группировка, агрегация и т.д.)
# - Поддержка различных форматов для ввода/вывода данных.

# Возможности matplotlib:
# - Создание различных типов графиков (линейные, барные и др.)
# - Настройка внешнего вида графиков (цвета, стили, метки)
# - Сохранение графиков в различных форматах (PNG, PDF и др.)
