import sqlite3


def initiate_db(name_db):
    connection = sqlite3.connect(f'{name_db}.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL)
    ''')
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products(title, description, price) VALUES (?, ?, ?)",
                       (f'Продукт{i}', f'Описание{i}', f'Цена: {i * 10}'))
    connection.commit()
    connection.close()


def get_all_products(db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute('SELECT title, description, price FROM Products')
    list_ = cursor.fetchall()
    all_prod = []
    for i in list_:
        result = (f'Название: {i[0]} | Описание: {i[1]} | {i[2]}')
        all_prod.append(result)
    return all_prod

