import sqlite3


def check_if_vaccine_has_spoiled(
        cursor: sqlite3.Cursor,
        truck_number: str
) -> bool:
    cursor.execute("""SELECT COUNT()
                      FROM `table_truck_with_vaccine`
                      WHERE truck_number=? AND temperature_in_celsius NOT BETWEEN 16 AND 20""", (truck_number,))
    return cursor.fetchone()[0] >= 3


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()

        print(check_if_vaccine_has_spoiled(cursor, 'т631вр78'))
