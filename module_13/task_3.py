import datetime
import sqlite3


def log_bird(
        cursor: sqlite3.Cursor,
        bird_name: str,
        date_time: str,
) -> None:
    if not check_if_such_bird_already_seen(cursor, bird_name):
        cursor.execute("""INSERT INTO `birds` (bird_name, datetime_added) VALUES (?, ?)""", (bird_name, date_time))


def check_if_such_bird_already_seen(
        cursor: sqlite3.Cursor,
        bird_name: str
) -> bool:
    cursor.execute("""SELECT EXISTS (SELECT * FROM `birds` WHERE bird_name=?)""", (bird_name,))
    return bool(cursor.fetchone()[0])


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS birds(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            bird_name VARCHAR(100) NOT NULL,
                            datetime_added DATATIME(100) NOT NULL)""")

        log_bird(cursor, 'titmouse', str(datetime.datetime.now()))
