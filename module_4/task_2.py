from flask import Flask
from flask_wtf import FlaskForm
from wtforms import Field, StringField, IntegerField
from wtforms.validators import InputRequired, Optional, Email, ValidationError

app = Flask(__name__)


def number_length(minlength, maxlength, message=None):
    if not message:
        message = f"Must be between {minlength} and {maxlength} characters long."

    def _number_length(form: FlaskForm, field: Field):
        length = len(str(field.data))
        if length > maxlength or length < minlength:
            raise ValidationError(message)

    return _number_length


class NumberLength:
    def __init__(self, minlength, maxlength, message=None):
        self.message = message
        self.maxlength = maxlength
        self.minlength = minlength

    def __call__(self, form: FlaskForm, field: Field):
        length = len(str(field.data))
        if length > self.maxlength or length < self.minlength:
            if not self.message:
                self.message = f"Must be between {self.minlength} and {self.maxlength} characters long."
            raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberLength(10, 11)])
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
