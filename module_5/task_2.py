import shlex
import subprocess

from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    time_out = IntegerField(validators=[InputRequired(), NumberRange(1, 30)])


@app.route('/code', methods=['POST'])
def code():
    form = CodeForm()
    if form.validate_on_submit():
        code = form.code.data
        time_out = form.time_out.data
        command = shlex.split(f'prlimit --nproc=1:1 python3 -c "{code}"')
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            out, errs = proc.communicate(timeout=time_out)
            return str(out.decode())
        except subprocess.TimeoutExpired:
            proc.kill()
            return f'команда выполнялась дольше указанного времени'
    else:
        return str(form.errors), 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
