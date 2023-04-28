import sqlite3

with sqlite3.connect('hw.db') as conn:
    cursor = conn.cursor()
    salary_ivan_sovin = \
    cursor.execute("""SELECT salary FROM `table_effective_manager` WHERE name='Иван Совин'""").fetchone()[0]


def ivan_sovin_the_most_effective(
        cursor: sqlite3.Cursor,
        name: str,
) -> None:
    cursor.execute("""UPDATE `table_effective_manager` SET salary= 
                      (SELECT salary FROM `table_effective_manager` WHERE name=?) * 1.1
                      WHERE name=?""", (name, name))

    cursor.execute("""DELETE FROM `table_effective_manager` WHERE name=? AND salary>?""", (name, salary_ivan_sovin))


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        ivan_sovin_the_most_effective(cursor, 'Михайлов В.Р.')
