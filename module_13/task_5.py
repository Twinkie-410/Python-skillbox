import sqlite3
import random

countries = ["Индия", "Китай", "США", "Индонезия", "Пакистан", "Нигерия", "Бразилия", "Бангладеш", "Россия", "Мексика",
             "Эфиопия"]


def generate_test_data(
        cursor: sqlite3.Cursor,
        number_of_groups: int
) -> None:
    cursor.execute("DELETE FROM 'uefa_commands'")
    cursor.execute("DELETE FROM 'uefa_draw'")
    levels = ["средняя", "сильная", "слабая"]

    for i in range(number_of_groups * 4):
        name = f'Team №{i + 1}'
        level = levels[0 if i % 4 == 3 else i % 4]
        country = random.choice(countries)
        cursor.execute("""INSERT INTO 'uefa_commands' VALUES (?, ?, ?, ?) """, (i + 1, name, country, level))
        cursor.execute("""INSERT INTO 'uefa_draw' VALUES (?, ?, ?)""", (i + 1, i + 1, i // 4))


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        generate_test_data(cursor, 5)
