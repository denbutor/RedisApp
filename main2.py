import json
import sqlite3
import redis

# conn = sqlite3.connect('database.db')
#
# # Створення курсора для виконання SQL-запитів
# curs = conn.cursor()
#
# # Створення таблиці users
# curs.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     Id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL
# );
# ''')
#
# # Додавання даних у таблицю
# curs.execute("INSERT INTO users (name) VALUES ('John Doe')")
# curs.execute("INSERT INTO users (name) VALUES ('Jane Smith')")
# curs.execute("INSERT INTO users (name) VALUES ('Alice Johnson')")
#
# # Підтвердження змін
# conn.commit()
#
# # Закриття з'єднання
# conn.close()

def get_my_friends():
    connection = sqlite3.connect(database='database.db')
    cursor = connection.cursor()
    redis_client = redis.Redis()

    cache_value = redis_client.get("user_friends")
    if cache_value is not None:
        return json.loads(cache_value)

    cursor.execute("SELECT Id, name FROM users;")
    result = cursor.fetchall()

    redis_client.set("user_friends", json.dumps(result), ex = 300)

    cursor.close()
    redis_client.close()
    return result

if __name__ == '__main__':
    print(get_my_friends())