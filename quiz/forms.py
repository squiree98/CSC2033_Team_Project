from flask import flash
from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError


def int_check(form, field):
    """Checks that the entered integer is
    between 1-4 and raises error if it is not


    :param form: form that integer is being entered on
    :type: form
    :param field: integer that is being checked
    :type: integer

    :author: Ewan Squire
    :date: 03/12/2021
    """
    if field.data > 4 or field.data < 1:
        flash('Please use an integer between 1 and 4 for answer field')
        raise ValidationError(f"Number must be between one and 4")


class CreateQuizForm(FlaskForm):
    """Form for create quiz form

    :param: FlaskForm
    :type: FlaskForm object

    :author: Ewan Squire
    :date: 02/12/2021
    """
    name = StringField(validators=[DataRequired()])
    age_group = SelectField(u'Age Range', choices=["5-12", "13-17", "18+"], validators=[DataRequired()])
    submit = SubmitField()


class CreateQuestionForm(FlaskForm):
    """Form for create question form

        :param: FlaskForm
        :type: FlaskForm object

        :author: Ewan Squire
        :date: 02/12/2021
        """
    question = StringField(validators=[DataRequired()])
    option_1 = StringField(validators=[DataRequired()])
    option_2 = StringField(validators=[DataRequired()])
    option_3 = StringField(validators=[DataRequired()])
    option_4 = StringField(validators=[DataRequired()])
    answer = IntegerField(validators=[DataRequired(), int_check])
    submit = SubmitField()


class SearchForm(FlaskForm):
    """
    Represents the search form (in the '/quizzes' page)

    author Kiara
    date 07/11/2021
    """
    email = StringField(validators=[DataRequired()])
    search = SubmitField()
