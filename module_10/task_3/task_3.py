import sqlite3

if __name__ == '__main__':
    with sqlite3.connect("hw_3_database.db") as conn:
        cursor = conn.cursor()

        # region 1
        for i in range(1, 4):
            execute = f"SELECT COUNT(ALL) FROM `table_{i}`"
            print(f"{cursor.execute(execute).fetchone()[0]} записей в таблице {i}")
        # endregion

        # region 2
        execute = "SELECT COUNT(DISTINCT value) FROM `table_1`"
        print(f"{cursor.execute(execute).fetchone()[0]} уникальных записей в таблице 1")
        # endregion

        # region 3
        execute = "SELECT value FROM `table_1` INTERSECT SELECT value FROM `table_2`"
        print(f"по {len(cursor.execute(execute).fetchall())} записям совпадают таблица 1 и таблица 2")
        # endregion

        # region 4
        execute = "SELECT value FROM `table_1` INTERSECT SELECT value FROM `table_2` INTERSECT SELECT value FROM `table_3`"
        print(f"по {len(cursor.execute(execute).fetchall())} записям совпадают все три таблицы")
        # endregion
