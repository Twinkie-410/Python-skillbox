import os.path

from flask import Flask

app = Flask(__name__)


@app.route("/preview/<int:size>/<path:relative_path>")
def preview(size, relative_path):
    abs_path = os.path.abspath(relative_path)
    with open(relative_path) as file:
        prev = file.read(size)
    return f"<b>{abs_path}</b> {size}<br>{prev}"


if __name__ == '__main__':
    app.run(debug=True)
