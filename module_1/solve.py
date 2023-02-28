from flask import Flask
import datetime
import re
import random

app = Flask(__name__)


@app.route("/hello_world")
def hello_world():
    return "Привет, мир!"
car_brands = ["Chevrolet", "Renault", "Ford", "Lada"]


@app.route("/cars")
def cars():
    return ", ".join(car_brands)
breeds = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]


@app.route("/cats")
def cats():
    return random.choice(breeds)


@app.route("/get_time/now")
def current_time():
    time = datetime.datetime.now()
    return f'Точное время: {time}'
file_text = open('war_and_peace.txt').read()


@app.route("/get_random_word")
def get_random_word():
    word = random.choice(get_words(file_text))
    return word


def get_words(text):
    return re.findall(r'[A-Za-zА-Яа-яёЁ]+', text)


@app.route("/counter")
def counter():
    counter.visits += 1
    return counter.visits.__str__()
counter.visits = 0

if __name__ == '__main__':
    app.run(debug=True)
