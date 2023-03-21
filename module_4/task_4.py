import uptime
from flask import Flask

app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime_at_now():
    return f'Current uptime is {uptime.uptime()}'


if __name__ == '__main__':
    app.run(debug=True)
