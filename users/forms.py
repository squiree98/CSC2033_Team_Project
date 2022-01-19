from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class RegisterForm(FlaskForm):
    """
    author Bogdan Ewan
    date 16/12/2021
    """
    # each data field must be error checked
    email = StringField(validators=[DataRequired(), Email()])

    password = PasswordField(validators=[DataRequired(), Length(min=8, max=15,
                                                message='Password must be between 8 and 15 characters in length.')])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    q1 = SelectField(u'Climate change causes an increase in temperature', choices=["TRUE", "FALSE"],
                     validators=[DataRequired()])
    q2 = SelectField(u'Burning fossil fuels does not cause climate change', choices=["TRUE", "FALSE"],
                     validators=[DataRequired()])
    q3 = SelectField(u'Climate change causes immense damage to our wildlife', choices=["TRUE", "FALSE"],
                     validators=[DataRequired()])
    q4 = SelectField(u'Climate change has yet to affect us', choices=["TRUE", "FALSE"], validators=[DataRequired()])
    q5 = SelectField(u'We need to act now', choices=["TRUE", "FALSE"], validators=[DataRequired()])
    submit = SubmitField()


class LoginForm(FlaskForm):
    """
    author Bogdan
    date 17/12/2021
    """
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()
