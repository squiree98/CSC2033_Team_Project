from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class CreateQuizForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    category = StringField(validators=[DataRequired()])


class CreateQuestionForm(FlaskForm):
    question = StringField(validators=[DataRequired()])
    option_1 = StringField(validators=[DataRequired()])
    option_2 = StringField(validators=[DataRequired()])
    option_3 = StringField(validators=[DataRequired()])
    option_4 = StringField(validators=[DataRequired()])
    answer = IntegerField(validators=[DataRequired()])