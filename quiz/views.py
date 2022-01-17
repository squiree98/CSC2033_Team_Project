from flask import Blueprint, render_template, redirect, url_for, session, flash
from flask_login import current_user, login_required
from sqlalchemy import desc
from models import Quiz, QuestionAndAnswers, Score, User
from quiz.forms import CreateQuestionForm, CreateQuizForm, SearchForm
from app import db, requires_roles

quiz_blueprint = Blueprint('quiz', __name__, template_folder='templates')


@quiz_blueprint.route('/quizzes', methods=['GET', 'POST'])
@login_required
def quizzes():
    """
    author Kiara
    date 30/11/2021
    """
    search = SearchForm()

    # check if handled request is a POST method
    if search.validate_on_submit():
        # display quizzes that match username given (in search)
        return search_quizzes(search)

    # get all quizzes that have not been created by currently logged-in user
    # and display the most recently created quizzes first
    view_quizzes = Quiz.query.filter(Quiz.user_id != current_user.id).order_by(desc('id')).all()
    # get leaderboards for quizzes leaderboard
    for x in range(len(view_quizzes)):
        # generate leaderboard for quiz
        user_leaderboard = get_leaderboard(view_quizzes[x].id)
        # add leaderboard to quiz's leaderboard value so it can be displayed in html
        view_quizzes[x].leaderboard = user_leaderboard
    return render_template('quizzes.html', form=search, quizzes=view_quizzes, filtered=False)


def get_leaderboard(quiz_id):
    # get all scores from scores table from highest to lowest
    scores = Score.query.filter_by(quiz_id=quiz_id).order_by(desc('score_value')).all()
    # create leaderboard to get score values
    trial_leaderboard = []
    # create leaderboard to organise values
    leaderboard = []
    # add scores
    if len(scores) == 0:
        trial_leaderboard = ["-", "-", "-"]
    if len(scores) == 1:
        trial_leaderboard = [scores[0], "-", "-"]
    if len(scores) == 2:
        trial_leaderboard = [scores[0], scores[1], "-"]
    if len(scores) >= 3:
        trial_leaderboard = [scores[0], scores[1], scores[2]]
    # for each score add a user
    for x in range(3):
        # if there's no score there is no user
        if trial_leaderboard[x] == "-":
            # convert to string statement
            leaderboard.append("Name: - Score: -")
        # if there's a score then find user that had score with scores user_id
        else:
            user = User.query.filter_by(id=trial_leaderboard[x].user_id).first()
            # convert to string statement
            leaderboard.append("Name: " + user.username + "Score: " + str(trial_leaderboard[x].score_value))
    return leaderboard


@quiz_blueprint.route("/search_quizzes")
@login_required
def search_quizzes(search):
    """

    author Kiara
    date 30/11/2021
    """

    search_string = search.email.data

    # retrieve the user with email address equal to the searched email address
    user = User.query.filter_by(email=search_string).first()

    # if valid email is entered
    if user:
        # check if currently logged-in user has entered their own email address
        if search_string == current_user.email:

            if current_user == 'user':
                flash('You cannot take your own quizzes. Go to "My Quizzes" to view the quizzes you have created.',
                      category='error')
            return redirect(url_for('quiz.quizzes'))

        quizzes = Quiz.query.filter_by(user_id=user.id).all()

        # if user has created quizzes, display their quizzes
        if quizzes:
            return render_template('quizzes.html', quizzes=quizzes, filtered=True)

        # display message if no quizzes have been created by user
        flash('No quizzes found.', category='error')
        return redirect(url_for('quiz.quizzes'))

    else:
        flash('Invalid Email Address. Try Again.', category='error')
        return redirect(url_for('quiz.quizzes'))


@quiz_blueprint.route('/<int:id>/report_quiz')
@login_required
@requires_roles('user')
def report_quiz(id):
    """
        :author Kiara
        :date 07/01/2022
    """

    # retrieve quiz from database
    quiz = Quiz.query.filter_by(id=id).first()
    # update number of reports (increment number of reports by 1)
    quiz.update_number_of_reports()
    return redirect(url_for("quiz.quizzes"))


@quiz_blueprint.route('/filter_by_age_group/<age_group>')
@login_required
@requires_roles('user')
def filter_by_age_group(age_group):
    """

    :author Kiara
    :date 07/01/2022
    """

    filtered_quizzes = Quiz.query.filter(Quiz.user_id != current_user.id, Quiz.age_group == age_group)
    return render_template('quizzes.html', quizzes=filtered_quizzes, filtered=True)


@quiz_blueprint.route('/filter_by_reported/')
@login_required
@requires_roles('admin')
def filter_by_reported():
    """

    :return:
    :author Kiara
    :date 07/01/2022
    """

    reported_quizzes = Quiz.query.filter(Quiz.user_id != current_user.id, Quiz.number_of_reports > 0).order_by(desc('number_of_reports')).all()
    return render_template('quizzes.html', quizzes=reported_quizzes, filtered=True)


@quiz_blueprint.route('/<int:id>/quiz_setup')
@login_required
@requires_roles('user')
def quiz_setup(id):
    """

    :param id:
    :return:
    :author Kiara
    :date 30/11/2021
    """

    session['quiz_id'] = id

    # retrieve quiz from database
    quiz = Quiz.query.filter_by(id=id).first()

    # reverse the order of the quiz questions
    quiz.questions_and_answers.reverse()

    # empty list for question_ids for quiz
    question_ids = []

    # add id for each question_and_answers to question_ids array
    for question_and_answers in quiz.questions_and_answers:
        question_ids.append(question_and_answers.id)

    # store question_ids array in a session variable
    session["question_ids"] = question_ids

    # initialise score session variable to zero
    session["score"] = 0

    return redirect(url_for('quiz.take_quiz'))


@quiz_blueprint.route('/take_quiz')
@login_required
@requires_roles('user')
def take_quiz():
    """

    :return:
    :author Kiara
    :date 30/11/2021
    """

    question_ids = session.get('question_ids')

    # if there are questions
    if question_ids:
        # get question id for next question
        question_id = question_ids.pop()
        # calculate question number (for progress bar)
        question_number = 10 - len(question_ids)
        # update question_ids session variable
        session['question_ids'] = question_ids
        # retrieve question and answers (options) from database for next question
        question_and_answers = QuestionAndAnswers.query.filter_by(id=question_id).first()
        # store correct answer for next question in answer session variable
        session['answer'] = question_and_answers.answer
        return render_template('take_quiz.html', question_number=question_number, question=question_and_answers)
    else:
        total_score_value = session.get('score')
        previous_score = Score.query.filter_by(quiz_id=session.get('quiz_id'), user_id=current_user.id).first()

        # if user has not played quiz before, store user's score in database
        if not previous_score:
            # create a Score instance to store user's score for quiz taken
            score = Score(session.get('quiz_id'), current_user.id, total_score_value)
            db.session.add(score)  # the new Score instance is added to database
            db.session.commit()  # database changes are committed

        # if user's current score is greater than previous score, update user's score value for quiz
        elif total_score_value > previous_score.score_value:
            previous_score.score_value = total_score_value
            db.session.commit()  # database changes are committed

        # retrieve quiz from database
        quiz = Quiz.query.filter_by(id=session.get('quiz_id')).first()
        # update number of plays for quiz (increment number of plays by 1)
        quiz.update_number_of_plays()

        return render_template("display_results.html", score=total_score_value, quiz_id=session.get('quiz_id'))


@quiz_blueprint.route('/<int:user_answer>/check_answer')
@login_required
@requires_roles('user')
def check_answer(user_answer):
    """
    :param user_answer:
    :return:

    author Kiara
    date 05/01/2021
    """
    # get user's score
    score = session.get('score')
    # get correct answer for current question
    correct_answer = session.get('answer')
    # if user chose correct answer increment score by 1
    if user_answer == correct_answer:
        score += 1
        session['score'] = score

    return redirect(url_for('quiz.take_quiz'))


@quiz_blueprint.route('/my_quizzes')
@login_required
@requires_roles('user')
def my_quizzes():
    return render_template('my_quizzes.html')


@quiz_blueprint.route('/create_quiz', methods=['GET', 'POST'])
@login_required
@requires_roles('user')
def create_quiz():
    # create form
    form = CreateQuizForm()
    # if the form is accepted
    if form.validate_on_submit():
        # create version of quiz
        # ToDo: Replace number with current_user_id
        user_id = 4
        # user_id = current_user.id
        new_quiz = [form.name.data, form.age_group.data, user_id]
        # create session and add data to session
        session['db_data'] = [new_quiz]
        # load the create question page
        return redirect(url_for('quiz.create_question'))
    # if form is invalid then reload the page and let them re-enter data
    return render_template('create_quiz.html', form=form)


@quiz_blueprint.route('/create_question', methods=['GET', 'POST'])
@login_required
@requires_roles('user')
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
            quiz_id = 10
            # quiz_id = Quiz.query.filter_by(id=current_user.id)
            # loop for every question
            for x in range(10):
                # convert session values into models object
                # x+1 because first value in session is the quiz not a question
                new_question = QuestionAndAnswers(question=db_data[x + 1][0], option_1=db_data[x + 1][1],
                                                  option_2=db_data[x + 1][2], option_3=db_data[x + 1][3],
                                                  option_4=db_data[x + 1][4], answer=db_data[x + 1][5], quiz_id=quiz_id)
                # add models object to database
                db.session.add(new_question)
                db.session.commit()
                return render_template('index.html')
    return render_template('create_question.html', form=form, question_num=len(db_data))


@quiz_blueprint.route('/<int:id>/delete_quiz')
@login_required
@requires_roles('user')
@login_required
def delete_quiz(id):
    """

    :param id:
    :return:
    author: Kiara
    date: 30/12/2021
    """
    Quiz.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for("quiz.quizzes"))