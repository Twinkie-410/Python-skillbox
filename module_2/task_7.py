import os.path

from flask import Flask

app = Flask(__name__)
storage = {}


@app.route("/add/<date>/<int:number>")
def add(date, number):
    if len(date) != 8:
        raise ValueError('Некорректная дата')
    storage.setdefault(date, 0)
    storage[date] += number

    storage.setdefault(date[:4], 0)
    storage[date[:4]] += number

    storage.setdefault(date[:6], 0)
    storage[date[:6]] += number
    # print(storage)
    return f"сумма {number} записана на дату {date[:4]}-{date[5:6]}-{date[7:]}"


@app.route("/calculate/<int:year>")
def calculate_year(year):
    return f"Суммарные траты за {year} год - {storage.setdefault(str(year), 0)}"


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(month, year):
    return f"Суммарные траты за {month} месяц {year} года - {storage.setdefault(str(year)+'{:02}'.format(month), 0)}"


if __name__ == '__main__':
    app.run(debug=True)
