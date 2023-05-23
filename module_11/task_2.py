import random
import sqlite3
import threading
import time

import requests

url = "https://swapi.dev/api/people/"
sql_request = "INSERT INTO persons (name, birth_year, gender) VALUES (?,?,?)"
persons = []


def get_random_person():
    response = requests.get(url + str(random.randint(1, 82)))
    if response.status_code == 200:
        person = dict(response.json())
        persons.append((person['name'], person['birth_year'], person['gender']))


def download_persons(cursor: sqlite3.Cursor):
    start = time.time()
    [get_random_person() for _ in range(20)]

    cursor.executemany(sql_request, persons)
    print(f"It took {(time.time() - start):0.4f}")


def download_person_many_threads(cursor: sqlite3.Cursor):
    start = time.time()
    threads = [threading.Thread(target=get_random_person) for _ in range(20)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]

    cursor.executemany(sql_request, persons)
    print(f"It took {(time.time() - start):0.4f}")


if __name__ == '__main__':
    with (sqlite3.connect('task_2.db')) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS persons (name text, birth_year text, gender text)")
        cursor.execute("DELETE FROM persons")

        # download_persons(cursor)  # It took 6.3393
        download_person_many_threads(cursor)  # It took 1.3924
