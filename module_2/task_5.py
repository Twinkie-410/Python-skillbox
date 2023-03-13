from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers>/")
def max_number(numbers):
    numbs = []
    for num in numbers.split('/'):
        if not num.isdigit():
            return f"<em>{num}</em> - не являеется числом"
        numbs.append(int(num))

    return f"Максимальное число: <em>{max(numbs)}<em>"


if __name__ == '__main__':
    app.run(debug=True)
