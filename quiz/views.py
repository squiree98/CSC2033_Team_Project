from flask import Blueprint, render_template

quiz_blueprint = Blueprint('quiz', __name__, template_folder='templates')


@quiz_blueprint.route('/quizzes')
def quizzes():
    return render_template('quizzes.html')


@quiz_blueprint.route('/my_quizzes')
def my_quizzes():
   return render_template('my_quizzes.html')


@quiz_blueprint.route('/take_quiz')
def take_quiz():
    return render_template('take_quiz.html')
