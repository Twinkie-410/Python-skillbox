from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, csrf
from wtforms.validators import *

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberRange(min=1_000_000_000, max=9_999_999_999)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField(validators=[Optional()])


@app.route("/registration", methods=['POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        name, email, phone, address, index, comment = \
            form.name.data, form.email.data, form.phone.data, form.address.data, form.index.data, form.comment.data
        return f"Пользователь успешно зарегистрирован:\n\tname: {name}\n\temail: {email}\n\tphone: {phone}\n\taddress: {address}\n\tindex: {index}\n\tcomment: {comment}"

    else:
        return str(form.errors), 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
