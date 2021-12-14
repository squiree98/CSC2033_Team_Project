from flask import Blueprint, render_template
from sqlalchemy import desc
from models import Quiz

quiz_blueprint = Blueprint('quiz', __name__, template_folder='templates')


@quiz_blueprint.route('/quizzes')
def quizzes():
    view_quizzes = Quiz.query.order_by(desc('id')).all()
    print(view_quizzes)
    return render_template('quizzes.html', quizzes=view_quizzes)


@quiz_blueprint.route('/my_quizzes')
def my_quizzes():
    return render_template('my_quizzes.html')


@quiz_blueprint.route('/<int:id>/take_quiz')
def take_quiz(id):
    print(id)
    return render_template('take_quiz.html')
