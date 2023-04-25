import sqlite3

if __name__ == '__main__':
    with sqlite3.connect("hw_2_database.db") as conn:
        cursor = conn.cursor()

        # region 1
        cursor.execute("SELECT * FROM 'table_checkout' ORDER BY sold_count DESC")
        print(f"Чаще покупают телефоны цвета {cursor.fetchone()[0]}({cursor.fetchone()[1]})")
        # endregion

        # region 2
        red = cursor.execute("SELECT * FROM 'table_checkout' WHERE phone_color='Red'").fetchone()
        blue = cursor.execute("SELECT * FROM 'table_checkout' WHERE phone_color='Blue'").fetchone()
        if red[1] > blue[1]:
            print(f"Чаще покупают телефоны цвета {red[0]}({red[1]}) нежели цвета {blue[0]}({blue[1]})")
        else:
            print(f"Чаще покупают телефоны цвета {blue[0]}({blue[1]}) нежели цвета {red[0]}({red[1]})")
        # endregion

        # region 3
        cursor.execute("SELECT * FROM 'table_checkout' ORDER BY sold_count")
        print(f"Реже покупают телефоны цвета {cursor.fetchone()[0]}({cursor.fetchone()[1]})")
        # endregion