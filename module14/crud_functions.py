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

    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()  # Получаем все записи

    conn.close()
    return products
