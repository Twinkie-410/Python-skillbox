import subprocess
from flask import Flask

app = Flask(__name__)


@app.route("/uptime", methods=['GET'])
def uptime_at_now():
    uptime_out = subprocess.run(['uptime', '--pretty'], capture_output=True).stdout.decode()
    return f'Current uptime is {uptime_out}'


if __name__ == '__main__':
    app.run(debug=True)
