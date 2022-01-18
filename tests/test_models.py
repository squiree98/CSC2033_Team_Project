"""
This file (test_models.py) contains the unit tests for the models.py file.
"""

from app import db
from models import User, Quiz, Score, QuestionAndAnswers


def test_new_user(client, init_database):
    """
    GIVEN a User model
    WHEN a new User is created and added to the database
    THEN check the fields for the new User are the same before and after a commit

    author Kiara
    date 18/01/2022
    """
    user_before_commit = User(username="Test", email="Test@email.com", password="password123", role="user",
                              subscribed=False)

    db.session.add(user_before_commit)
    db.session.commit()

    # get new_user from database
    user_after_commit = User.query.filter_by(id=user_before_commit.id).first()

    assert user_before_commit.email == user_after_commit.email
    assert user_before_commit.username == user_after_commit.username
    assert user_before_commit.password == user_after_commit.password


def test_new_quiz(client, init_database):
    """
    GIVEN a Quiz model
    WHEN a new Quiz is created and added to the database
    THEN check the fields for the new Quiz are the same before and after a commit

    author Kiara
    date 18/01/2022
    """

    quiz_before_commit = Quiz(user_id=1, name="Climate Action", age_group="5-12")
    db.session.add(quiz_before_commit)  # add quiz object to the database
    db.session.commit()  # commit changes to database

    # get Quiz object from database
    quiz_after_commit = Quiz.query.filter_by(id=quiz_before_commit.id).first()

    assert quiz_before_commit.user_id == quiz_after_commit.user_id
    assert quiz_before_commit.name == quiz_after_commit.name
    assert quiz_before_commit.age_group == quiz_after_commit.age_group


def test_new_question_and_answers(client, init_database):
    """
    GIVEN a QuestionAndAnswer model
    WHEN a new QuestionAndAnswer is created and added to the database
    THEN check the fields for the new QuestionAndAnswer are the same before and after a commit

    author Kiara
    date 18/01/2022
    """

    question_and_answers_before_commit = QuestionAndAnswers(quiz_id=1, question="Question 1", option_1="A",
                                                            option_2="B", option_3="C", option_4="D", answer=1)

    db.session.add(question_and_answers_before_commit)
    db.session.commit()

    # get QuestionAndAnswer object from database
    question_and_answers_after_commit = QuestionAndAnswers.query.filter_by(id=question_and_answers_before_commit.id).first()

    assert question_and_answers_before_commit.question == question_and_answers_after_commit.question
    assert question_and_answers_before_commit.option_1 == question_and_answers_after_commit.option_1
    assert question_and_answers_before_commit.option_2 == question_and_answers_after_commit.option_2
    assert question_and_answers_before_commit.option_3 == question_and_answers_after_commit.option_3
    assert question_and_answers_before_commit.option_4 == question_and_answers_after_commit.option_4


def test_new_score(client, init_database):
    """
    GIVEN a Score model
    WHEN a new Score is created and added to the database
    THEN check the fields for the new Score are the same before and after a commit

    author Kiara
    date 18/01/2022
    """

    score_before_commit = Score(quiz_id=1, user_id=1, score_value=10)

    db.session.add(score_before_commit)
    db.session.commit()

    # get Score object from database
    score_after_commit = Score.query.filter_by(id=score_before_commit.id).first()

    assert score_before_commit.quiz_id == score_after_commit.quiz_id
    assert score_before_commit.user_id == score_after_commit.user_id
    assert score_before_commit.score_value == score_after_commit.score_value

