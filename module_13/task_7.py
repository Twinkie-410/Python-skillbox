import sqlite3


def register(username: str, password: str) -> None:
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        cursor.executescript(
            f"""
            INSERT INTO `table_users` (username, password)
            VALUES ('{username}', '{password}')  
            """
        )
        conn.commit()


def hack() -> None:
    username: str = "someusername"
    password: str = "somepassword'); DELETE FROM table_users; --" #или любой другой sql запрос
    register(username, password)


if __name__ == '__main__':
    hack()
