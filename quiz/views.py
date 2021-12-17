from flask import Blueprint, render_template, redirect, url_for, session
from sqlalchemy import desc
from models import Quiz, QuestionAndAnswers
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
        new_quiz = [form.name.data, form.age_range.data, 2]
        # create session and add data to session
        session['db_data'] = [new_quiz]
        # load the create question page
        return redirect(url_for('quiz.create_question'))
    # if form is invalid then reload the page and let them re-enter data
    return render_template('create_quiz.html', form=form)


@quiz_blueprint.route('/create_question', methods=['GET', 'POST'])
def create_question():
    # create form for create question
    form = CreateQuestionForm()
    # if form details are accepted
    if form.validate_on_submit():
        # get session to add data
        db_data = session.get('db_data')
        if len(db_data) == 11:
            # add quiz details to database
            new_quiz = Quiz(name=db_data[0][0], age_group=db_data[0][1], user_id=db_data[0][2])
            db.session.add(new_quiz)
            db.session.commit()
            # ToDo: query database for quiz ID
            for x in range(10):
                new_question = QuestionAndAnswers(question=form.question.data, option_1=form.option_1.data,
                                                  option_2=form.option_2.data, option_3=form.option_3.data,
                                                  option_4=form.option_4.data, answer=form.answer.data, quiz_id=10)
                # ToDo: replace value with quiz ID
    return render_template('create_question.html', form=form)