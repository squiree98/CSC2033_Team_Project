from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    # each data field must be error checked
    email = StringField(validators=[DataRequired()])
    firstName = StringField(validators=[DataRequired()])
    lastName = StringField(validators=[DataRequired()])

    password = PasswordField(validators=[DataRequired(), Length(min=8, max=16, message="Password must be between 8"
                                                                                       " and 16 characters")])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password', message="Password do not match")])
    submit = SubmitField()
