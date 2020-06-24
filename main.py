import sqlite3
from sqlite3 import Error

create_users_table = """
CREATE TABLE IF NOT EXISTS `users` (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    nationality TEXT
);
"""

create_posts_table = """
CREATE TABLE IF NOT EXISTS posts(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

# Соединение с ьд
def create_connection(path):
    connection = None
    try:
        # Подлючается к базе данных 
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# Выполняет запрос для бд
def execute_query(connection, query):
    # Хуйня что бы вызвать мето execute который выполнеяет запрос
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print('Query executed successfully')
    except Error as e:
        print(f"The error '{e}' occurred")


connect = create_connection('first_db')
execute_query(connect, create_posts_table)
