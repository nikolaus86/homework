import sqlite3

# Создаем и подключаемся к базе данных
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# (Предполагается, что таблица уже создана и заполнена)

# Удаляем запись с id = 6
cursor.execute('DELETE FROM Users WHERE id = 6')

# Подсчитываем общее количество записей
cursor.execute('SELECT COUNT(*) FROM Users')
total_records = cursor.fetchone()[0]
print(f"Общее количество записей: {total_records}")

# Считаем сумму всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]

# Вычисляем средний баланс
if total_records > 0:
    average_balance = total_balance / total_records
    print(f"Средний баланс всех пользователей: {average_balance:.2f}")
else:
    print("Нет записей для вычисления среднего баланса.")

# Закрываем соединение с базой данных
conn.commit()
conn.close()
