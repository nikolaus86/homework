import sqlite3

def initiate_db():
    conn = sqlite3.connect('products.db')  # Создаем или открываем базу данных
    cursor = conn.cursor()

    # Создаем таблицу Products, если она ещё не создана
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')

    # Создаем таблицу Users, если она ещё не создана
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL DEFAULT 1000
    )
    ''')

    conn.commit()
    conn.close()


def add_user(username, email, age):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Users (username, email, age) VALUES (?, ?, ?)
    ''', (username, email, age))

    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT username FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()  # Получаем запись

    conn.close()
    return user is not None


def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()  # Получаем все записи

    conn.close()
    return products
