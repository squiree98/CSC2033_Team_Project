from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError


def int_check(form, field):
    if field.data > 4 or field.data < 1:
        raise ValidationError(f"Number must be between one and 4")


class CreateQuizForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    age_range = SelectField(u'Age Range', choices=["5-12", "13-18", "18+"], validators=[DataRequired()])
    submit = SubmitField()


class CreateQuestionForm(FlaskForm):
    question = StringField(validators=[DataRequired()])
    option_1 = StringField(validators=[DataRequired()])
    option_2 = StringField(validators=[DataRequired()])
    option_3 = StringField(validators=[DataRequired()])
    option_4 = StringField(validators=[DataRequired()])
    answer = IntegerField(validators=[DataRequired(), int_check])
    submit = SubmitField()
