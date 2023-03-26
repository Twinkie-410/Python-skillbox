import os
import subprocess

from flask import Flask


def vacate_port(port: int):
    lsof_info = subprocess.run(['lsof', '-i', f':{port}'], capture_output=True).stdout.decode()
    pids = [int(proc.split()[1]) for proc in lsof_info.split('\n')[1:] if len(proc) >= 2]
    print(pids)
    if len(pids) > 0:
        [os.kill(pid, 9) for pid in pids]


app = Flask(__name__)


@app.route('/test_port')
def test_port():
    return f'сервер запущен'


if __name__ == '__main__':
    port = 5000
    vacate_port(port)
    app.run(port=port)
