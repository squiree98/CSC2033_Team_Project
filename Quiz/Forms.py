from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CreateQuizForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    category = StringField(validators=[DataRequired()])
