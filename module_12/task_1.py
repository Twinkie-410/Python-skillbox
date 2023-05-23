import multiprocessing
import random
import sqlite3
import threading
import time
from multiprocessing import Pool
from multiprocessing.pool import ThreadPool

import requests

url = "https://swapi.dev/api/people/"
sql_request = "INSERT INTO persons (name, birth_year, gender) VALUES (?,?,?)"


# persons = []


def get_random_person(*args):
    response = requests.get(url + str(random.randint(1, 82)))
    if response.status_code == 200:
        person = dict(response.json())
        return person['name'], person['birth_year'], person['gender']
    else:
        return get_random_person()


def download_persons_pool(cursor: sqlite3.Cursor):
    start = time.time()
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        persons = list(pool.map(get_random_person, [_ for _ in range(20)]))

    print(f"It took {(time.time() - start):0.4f}")
    cursor.executemany(sql_request, persons)


def download_person_threadpool(cursor: sqlite3.Cursor):
    start = time.time()
    with ThreadPool(processes=20) as pool:
        persons = list(pool.map(get_random_person, [_ for _ in range(20)]))

    print(f"It took {(time.time() - start):0.4f}")
    cursor.executemany(sql_request, persons)


if __name__ == '__main__':
    with (sqlite3.connect('task_1.db')) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS persons (name text, birth_year text, gender text)")
        cursor.execute("DELETE FROM persons")

        download_persons_pool(cursor)  # 1.8263
        download_person_threadpool(cursor)  # 0.6124
