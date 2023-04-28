import sqlite3
import csv


def delete_wrong_fees(
        cursor: sqlite3.Cursor,
        wrong_fees_file: str
) -> None:
    with open(wrong_fees_file, 'r', encoding='windows-1251') as wrong_fees:
        reader = csv.reader(wrong_fees)
        reader.__next__()
        for line in reader:
            cursor.execute("""DELETE FROM `table_fees` 
                              WHERE truck_number=? AND timestamp=?""", (line[0], line[1]))


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()

        delete_wrong_fees(cursor, 'wrong_fees.csv')
