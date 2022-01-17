from flask_login import UserMixin

from app import db
from datetime import datetime
import bcrypt


def hashPwd(pwd):
    bpwd = pwd.encode()
    salt = bcrypt.gensalt()
    hashedpwd = bcrypt.hashpw(bpwd,salt)
    return hashedpwd


def init_db():
    """

    authors Kiara, Bogdan, Ewan
    date:
    """
    # delete database tables (if they exist)
    db.drop_all()
    # create database tables
    db.create_all()

    # add sample data to database
    add_sample_data()


def add_sample_data():
    # USERS
    # with 'user' role
    user1 = User(username="User1", email="User1@email.com",
                 password="$2b$12$WVjfaXCpS8fFPRMClIqnAulf8oHTGUGSlIzKJ9rQ1ZtmLiOG7tuf", role="user", subscribed=False)
    user2 = User(username="User2", email="User2@email.com",
                 password="$2b$12$WVjfaXCpS8fFPRMClIqnAulf8oHTGUGSlIzKJ9rQ1ZtmLiOG7tuf", role="user", subscribed=False)
    user3 = User(username="User3", email="User3@email.com",
                 password="$2b$12$WVjfaXCpS8fFPRMClIqnAulf8oHTGUGSlIzKJ9rQ1ZtmLiOG7tuf", role="user", subscribed=False)
    user4 = User(username="User4", email="User4@email.com",
                 password="$2b$12$WVjfaXCpS8fFPRMClIqnAulf8oHTGUGSlIzKJ9rQ1ZtmLiOG7tuf", role="user", subscribed=False)

    # with 'admin' role
    admin1 = User(username="Admin1", email="Admin1@email.com",
                  password="$2b$12$WVjfaXCpS8fFPRMClIqnAulf8oHTGUGSlIzKJ9rQ1ZtmLiOG7tuf", role="admin",
                  subscribed=False)
    admin2 = User(username="Admin2", email="Admin2@email.com",
                  password="$2b$12$WVjfaXCpS8fFPRMClIqnAulf8oHTGUGSlIzKJ9rQ1ZtmLiOG7tuf", role="admin",
                  subscribed=False)

    db.session.add_all([user1, user2, user3, user4, admin1, admin2])  # add users to database
    db.session.commit()  # commit changes

    # QUIZZES
    # created by user1
    quiz1 = Quiz(user1.id, "What is climate change?", "5-12")
    # TODO: questions and answers for quiz1

    quiz2 = Quiz(user1.id, "?", "13-17")
    # TODO: questions and answers for quiz1


    quiz3 = Quiz(user1.id, "?", "18+")
    # TODO: questions and answers for quiz1

    db.session.add_all([quiz1, quiz2, quiz3])  # add quizzes to database
    db.session.commit()  # commit changes

    # SCORES
    # for quiz1
    score1 = Score(quiz1.id, user2.id, 10)
    score2 = Score(quiz1.id, user3.id, 10)
    score3 = Score(quiz1.id, user4.id, 7)

    # for quiz2
    score4 = Score(quiz2.id, user2.id, 5)
    score5 = Score(quiz2.id, user3.id, 3)

    db.session.add_all([score1, score2, score3, score4, score5])  # add scores to database
    db.session.commit()  # commit changes


class User(db.Model, UserMixin):
    """

       authors Kiara, Bogdan, Ewan
       date:
    """
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
        self.password = hashPwd(password)
        self.role = role
        self.subscribed = subscribed
        self.registered_on = datetime.now()
        self.last_logged_in = None
        self.currently_logged_in = None
        self.average_score = 0


class Quiz(db.Model):
    """

       authors Kiara, Bogdan, Ewan
       date:
    """
    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)  # foreign key
    name = db.Column(db.Text, nullable=False, default=False)
    age_group = db.Column(db.String(100))
    number_of_plays = db.Column(db.Integer)
    number_of_reports = db.Column(db.Integer)

    scores = db.relationship('Score')
    questions_and_answers = db.relationship('QuestionAndAnswers')

    def __init__(self, user_id, name, age_group):
        self.user_id = user_id
        self.name = name
        self.age_group = age_group
        self.number_of_plays = 0
        self.number_of_reports = 0
        self.leaderboard = []

    def update_number_of_plays(self):
        """

        author Kiara
        date 07/01/2021
        """
        # increment number of plays by 1
        self.number_of_plays += 1
        db.session.commit()

    def update_number_of_reports(self):
        """

        author Kiara
        date 07/01/2021
        """
        # increment number of reports by 1
        self.number_of_reports += 1
        db.session.commit()


class Score(db.Model):
    """

       authors Kiara, Bogdan, Ewan
       date:
    """
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
    """

    authors Kiara, Bogdan, Ewan
    date:
    """
    __tablename__ = 'question_and_answers'

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey(Quiz.id), nullable=False)  # foreign key
    question = db.Column(db.Text, nullable=False, default=False)
    option_1 = db.Column(db.Text, nullable=False, default=False)
    option_2 = db.Column(db.Text, nullable=False, default=False)
    option_3 = db.Column(db.Text, nullable=False, default=False)
    option_4 = db.Column(db.Text, nullable=False, default=False)
    answer = db.Column(db.Integer, nullable=False, default=False)

    def __init__(self, quiz_id, question, option_1, option_2, option_3, option_4, answer):
        self.quiz_id = quiz_id
        self.question = question
        self.option_1 = option_1
        self.option_2 = option_2
        self.option_3 = option_3
        self.option_4 = option_4
        self.answer = answer
