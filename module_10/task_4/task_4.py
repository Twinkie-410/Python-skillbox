import sqlite3


def take_median(salaries):
    if len(salaries) % 2 == 0:
        return round((salaries[len(salaries) // 2][0] + salaries[len(salaries) // 2 + 1][0]) / 2, 2)
    else:
        return salaries[len(salaries) // 2][0]


if __name__ == '__main__':
    with sqlite3.connect("hw_4_database.db") as conn:
        cursor = conn.cursor()

        # region 1
        execute = "SELECT COUNT() FROM `salaries` WHERE (salary < 5000)"
        print(f"{cursor.execute(execute).fetchone()[0]} человек находятся за чертой бедности")
        # endregion

        # region 2
        execute = "SELECT ROUND(AVG(salary), 2) FROM `salaries`"
        print(f"{cursor.execute(execute).fetchone()[0]} - средняя З/П")
        # endregion

        # region 3
        execute = "SELECT salary FROM `salaries` ORDER BY salary"
        salaries = cursor.execute(execute).fetchall()
        print(f"{take_median(salaries)} - медианная З/П")
        # endregion

        # region 4
        count = cursor.execute("SELECT COUNT() FROM `salaries`").fetchone()[0]
        total_salary = cursor.execute("SELECT SUM(salary) FROM `salaries`").fetchone()[0]
        execute = f"SELECT SUM(salary) FROM (SELECT salary FROM `salaries` ORDER BY salary DESC LIMIT {count} * 0.1)"
        top10_salary = cursor.execute(execute).fetchone()[0]
        top90_salary = total_salary - top10_salary
        print(f"{round(top10_salary / top90_salary * 100, 2)}% социального неравенства")
        # endregion
