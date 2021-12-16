from flask_login import UserMixin

from app import db
from datetime import datetime


def init_db():
    new_user = User(username="Admin", email="Admin@email.com", password="AdminPassword", role="Admin", subscribed=False)
    db.drop_all()
    db.create_all()
    db.session.add(new_user)
    db.session.commit()


def temporary_data():
    new_quiz = Quiz(user_id=5, name="Climate Action", age_group="13-17")
    db.session.add(new_quiz)
    db.session.commit()


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    subscribed = db.Column(db.Boolean, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    last_logged_in = db.Column(db.DateTime, nullable=True)
    currently_logged_in = db.Column(db.DateTime, nullable=True)
    average_score = db.Column(db.Integer, nullable=True)

    created_quiz = db.relationship('Quiz')
    quiz_scores = db.relationship('Score')

    def __init__(self, username, email, password, role, subscribed):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.subscribed = subscribed
        self.registered_on = datetime.now()
        self.last_logged_in = None
        self.currently_logged_in = None
        self.average_score = 0


class Quiz(db.Model):
    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)  # foreign key
    name = db.Column(db.Text, nullable=False, default=False)
    age_group = db.Column(db.String(100), primary_key=True)
    number_of_plays = db.Column(db.Integer, primary_key=True)

    scores = db.relationship('Score')
    questions_and_answers = db.relationship('QuestionAndAnswers')

    def __init__(self, user_id, name, age_group):
        self.user_id = user_id
        self.name = name
        self.age_group = age_group
        self.number_of_plays = 0


class Score(db.Model):
    __tablename__ = 'score'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # foreign keys
    quiz_id = db.Column(db.Integer, db.ForeignKey(Quiz.id), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    score_value = db.Column(db.Integer, nullable=False)

    def __init__(self, quiz_id, user_id, score_value):
        self.quiz_id = quiz_id
        self.user_id = user_id
        self.score_value = score_value


class QuestionAndAnswers(db.Model):
    __tablename__ = 'question_and_answers'

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey(Quiz.id), nullable=False)  # foreign key
    question = db.Column(db.Text, nullable=False, default=False)
    option_1 = db.Column(db.Text, nullable=False, default=False)
    option_2 = db.Column(db.Text, nullable=False, default=False)
    option_3 = db.Column(db.Text, nullable=False, default=False)
    answer = db.Column(db.Text, nullable=False, default=False)

    def __init__(self, quiz_id, question, option_1, option_2, option_3, answer):
        self.quiz_id = quiz_id
        self.question = question
        self.option_1 = option_1
        self.option_2 = option_2
        self.option_3 = option_3
        self.answer = answer
