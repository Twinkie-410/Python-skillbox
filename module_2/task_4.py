import sys
from flask import Flask
from datetime import datetime

good_weekday_tuple = (
    "Хорошего понедельника", "Хорошего вторника", "Хорошей среды", "Хорошего четверга", "Хорошеё пятницы",
    "Хорошей субботы", "Хорошего воскресенья")
good_weekday_list = [
    "Хорошего понедельника", "Хорошего вторника", "Хорошей среды", "Хорошего четверга", "Хорошеё пятницы",
    "Хорошей субботы", "Хорошего воскресенья"]
good_weekday_dict = {
    0: "Хорошего понедельника", 1: "Хорошего вторника", 2: "Хорошей среды", 3: "Хорошего четверга",
    4: "Хорошеё пятницы",
    5: "Хорошей субботы", 6: "Хорошего воскресенья"}
# print(sys.getsizeof(good_weekday_tuple))
# print(sys.getsizeof(good_weekday_list))
# print(sys.getsizeof(good_weekday_dict))

app = Flask(__name__)


@app.route("/hello_world/<name>/")
def hello_world(name):
    weekday = datetime.today().weekday()
    return f"Привет, {name}. {good_weekday_tuple[weekday]}!"


if __name__ == '__main__':
    app.run(debug=True)
