from flask import Flask, request

app = Flask(__name__)


@app.route("/log_save", methods=["POST"])
def save():
    data = request.form.to_dict()
    with open("./server.log", "a") as file_log:
        log = f"{data['level']} | {data['name']} | {data['asctime']} | {data['msg']}\n"
        file_log.write(log)
        return "лог сохранён"


@app.route("/log_get", methods=["GET"])
def get_log():
    with open("./server.log", "r") as log:
        return log.read()


if __name__ == '__main__':
    app.run(debug=True)
