from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(FlaskForm):
    # each data field must be error checked
    email = StringField(validators=[DataRequired(), Email()])

    password = PasswordField(validators=[DataRequired(), Length(min=8, max=15,message='Password must be between 8 and 15 characters in length.')])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    q1 = StringField(validators=[DataRequired()])
    q2 = StringField(validators=[DataRequired()])
    q3 = StringField(validators=[DataRequired()])
    q4 = StringField(validators=[DataRequired()])
    q5 = StringField(validators=[DataRequired()])
    submit = SubmitField()


class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()
