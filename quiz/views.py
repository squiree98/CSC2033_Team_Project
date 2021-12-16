from flask import Blueprint, render_template
from sqlalchemy import desc
from models import Quiz
from quiz.forms import CreateQuestionForm, CreateQuizForm
from app import db

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


@quiz_blueprint.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():
    # create form
    form = CreateQuizForm()
    # if the form is accepted
    if form.validate_on_submit():
        # create version of quiz
        new_quiz = Quiz(name=form.name.data,
                        age_group=form.age_range.data,
                        user_id=2)
        # and add it too the database
        db.session.add(new_quiz)
        db.session.commit()
        # load the create question page
        create_question()
    # if form is invalid then reload the page and let them re-enter data
    return render_template('create_quiz.html', form=form)


def create_question():
    form = CreateQuestionForm
    return render_template('create_question.html', form=form)