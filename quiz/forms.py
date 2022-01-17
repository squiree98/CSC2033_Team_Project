from flask import flash
from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError


def int_check(form, field):
    if field.data > 4 or field.data < 1:
        flash('Please use an integer between 1 and 4 for answer field')
        raise ValidationError(f"Number must be between one and 4")


class CreateQuizForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    age_group = SelectField(u'Age Range', choices=["5-12", "13-17", "18+"], validators=[DataRequired()])
    submit = SubmitField()


class CreateQuestionForm(FlaskForm):
    question = StringField(validators=[DataRequired()])
    option_1 = StringField(validators=[DataRequired()])
    option_2 = StringField(validators=[DataRequired()])
    option_3 = StringField(validators=[DataRequired()])
    option_4 = StringField(validators=[DataRequired()])
    answer = IntegerField(validators=[DataRequired(), int_check])
    submit = SubmitField()


class SearchForm(FlaskForm):
    """
    author Kiara
    date 07/11/2021
    """
    email = StringField(validators=[DataRequired()])
    search = SubmitField()
