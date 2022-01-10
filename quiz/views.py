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
        # ToDo: Replace 2 with current_user_id
        new_quiz = [form.name.data, form.age_range.data, 4]
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
    db_data = session.get('db_data')
    if form.validate_on_submit():
        # get session to add data
        print(db_data)
        # if form is valid add it's details to session
        db_data.append([form.question.data, form.option_1.data, form.option_2.data, form.option_3.data,
                        form.option_4.data, form.answer.data])
        session['db_data'] = db_data
        # if session is length 11 then quiz and all questions have been created
        if len(db_data) == 11:
            # add quiz details to database
            new_quiz = Quiz(name=db_data[0][0], age_group=db_data[0][1], user_id=db_data[0][2])
            db.session.add(new_quiz)
            db.session.commit()
            # add questions to db
            # ToDo: query database for quiz ID and replace quiz_id below with it
            # loop for every question
            for x in range(10):
                # convert session values into models object
                # x+1 because first value in session is the quiz not a question
                new_question = QuestionAndAnswers(question=db_data[x + 1][0], option_1=db_data[x + 1][1],
                                                  option_2=db_data[x + 1][2], option_3=db_data[x + 1][3],
                                                  option_4=db_data[x + 1][4], answer=db_data[x + 1][5], quiz_id=10)
                # add models object to database
                db.session.add(new_question)
                db.session.commit()
                return render_template('index.html')
    return render_template('create_question.html', form=form, question_num=len(db_data))
