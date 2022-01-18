from flask_login import UserMixin

from app import db
from datetime import datetime
import bcrypt


def hash_pwd(pwd):
    bpwd = pwd.encode()
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(bpwd, salt)
    return hashed_pwd


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
    quiz1 = Quiz(user1.id, "What is global warming?", "5-12")

    quiz2 = Quiz(user1.id, "Climate Action", "18+")

    quiz3 = Quiz(user1.id, "Greenhouse Gases", "13-17")

    db.session.add_all([quiz1, quiz2, quiz3])  # add quizzes to database
    db.session.commit()  # commit changes

    # QUESTIONANDANSWER
    # for quiz 1
    quiz1_question_and_answer_1 = QuestionAndAnswers(1, "Question 1", "A", "B", "C", "D", 1)
    quiz1_question_and_answer_2 = QuestionAndAnswers(1, "Question 2", "A", "B", "C", "D", 1)
    quiz1_question_and_answer_3 = QuestionAndAnswers(1, "Question 3", "A", "B", "C", "D", 1)
    quiz1_question_and_answer_4 = QuestionAndAnswers(1, "Question 4", "A", "B", "C", "D", 1)
    quiz1_question_and_answer_5 = QuestionAndAnswers(1, "Question 5", "A", "B", "C", "D", 1)
    quiz1_question_and_answer_6 = QuestionAndAnswers(1, "Question 6", "A", "B", "C", "D", 1)
    quiz1_question_and_answer_7 = QuestionAndAnswers(1, "Question 7", "A", "B", "C", "D", 1)
    quiz1_question_and_answer_8 = QuestionAndAnswers(1, "Question 8", "A", "B", "C", "D", 1)
    quiz1_question_and_answer_9 = QuestionAndAnswers(1, "Question 9", "A", "B", "C", "D", 1)
    quiz1_question_and_answer_10 = QuestionAndAnswers(1, "Question 10", "A", "B", "C", "D", 1)

    # for quiz 2
    quiz2_question_and_answer_1 = QuestionAndAnswers(2, "Question 1", "A", "B", "C", "D", 1)
    quiz2_question_and_answer_2 = QuestionAndAnswers(2, "Question 2", "A", "B", "C", "D", 1)
    quiz2_question_and_answer_3 = QuestionAndAnswers(2, "Question 3", "A", "B", "C", "D", 1)
    quiz2_question_and_answer_4 = QuestionAndAnswers(2, "Question 4", "A", "B", "C", "D", 1)
    quiz2_question_and_answer_5 = QuestionAndAnswers(2, "Question 5", "A", "B", "C", "D", 1)
    quiz2_question_and_answer_6 = QuestionAndAnswers(2, "Question 6", "A", "B", "C", "D", 1)
    quiz2_question_and_answer_7 = QuestionAndAnswers(2, "Question 7", "A", "B", "C", "D", 1)
    quiz2_question_and_answer_8 = QuestionAndAnswers(2, "Question 8", "A", "B", "C", "D", 1)
    quiz2_question_and_answer_9 = QuestionAndAnswers(2, "Question 9", "A", "B", "C", "D", 1)
    quiz2_question_and_answer_10 = QuestionAndAnswers(2, "Question 10", "A", "B", "C", "D", 1)

    # for quiz 3
    quiz3_question_and_answer_1 = QuestionAndAnswers(3, "What is the greenhouse effect?",
                                                     "Certain gases in the atmosphere trap heat and warm the Earth",
                                                     "Life on Earth 'exhales' gas that warms up the atmosphere",
                                                     "The tilt of the Earth changes the amount of solar energy the Earth receives",
                                                     "The Sun is putting out more radiant energy over time", 1)
    quiz3_question_and_answer_2 = QuestionAndAnswers(3, "The greenhouse effect occurs because gases in the atmosphere trap energy from the sun. "
                                                        "Which of the following is not greenhouse gas? ",
                                                     "Carbon dioxide", "Methane", "Water vapour", "Nitrogen", 4)
    quiz3_question_and_answer_3 = QuestionAndAnswers(3, "What do greenhouse gases do in our atmosphere? ",
                                                     "These gases absorb the sun heat & emits radiant energy ",
                                                     "These gases keep all the air within the Earth",
                                                     "Increases the Earth's temperature ",
                                                     "It makes the Earth cooler ", 1)
    quiz3_question_and_answer_4 = QuestionAndAnswers(3, "Which country has emitted the most CO2?",
                                                     "China", "USA", "Russia", "Saudi Arabia", 2)
    quiz3_question_and_answer_5 = QuestionAndAnswers(3, "How long does CO2 remain in the atmosphere?",
                                                     "CO2 washes out of the atmosphere seasonally.",
                                                     "CO2 remains in the atmosphere for 5-10 years.",
                                                     "CO2 remains in the atmosphere for up to 200 years, or more.",
                                                     "C02 remains in the atmosphere for 100 years", 3)
    quiz3_question_and_answer_6 = QuestionAndAnswers(3, "When was the last time in Earth's history that CO2 was as high as it is now?",
                                                     "This is the highest it's ever been",
                                                     "CO2 was at least this high during the warm periods between the ice ages",
                                                     "CO2 has not been this high for almost one million years.",
                                                     "The last time CO2 was this high was 3 million years ago", 3)
    quiz3_question_and_answer_7 = QuestionAndAnswers(3, "Which of these activities is the largest contributor of greenhouse gases?",
                                                     "Deforestation",
                                                     "Transportation",
                                                     "Landfills",
                                                     "Agriculture", 2)
    quiz3_question_and_answer_8 = QuestionAndAnswers(3, "What are the major causes of sea level rise?",
                                                     "Melting sea ice", "Melting glaciers and ice sheets",
                                                     "Rivers accelerating", "Rocks and soil washing into the sea", 2)
    quiz3_question_and_answer_9 = QuestionAndAnswers(3, "Cattle farming results in which of the following greenhouse gases",
                                                     "Nitrous oxide",
                                                     "Carbon monoxide",
                                                     "Methane",
                                                     "Water vapour", 3)
    quiz3_question_and_answer_10 = QuestionAndAnswers(3, "Gas molecules that absorb thermal infrared radiation and are present in large quantity "
                                                         "to alter the climate system is known as",
                                                      "Greenhouse gases",
                                                      "Beta radiations",
                                                      "Alpha radiations",
                                                      "Ozone gases", 1)

    # add question_and_answers to database
    db.session.add_all([quiz1_question_and_answer_1, quiz1_question_and_answer_2, quiz1_question_and_answer_3,
                        quiz1_question_and_answer_4,  quiz1_question_and_answer_5,  quiz1_question_and_answer_6,
                        quiz1_question_and_answer_7, quiz1_question_and_answer_8,  quiz1_question_and_answer_9,
                        quiz1_question_and_answer_10,
                        quiz2_question_and_answer_1, quiz2_question_and_answer_2,
                        quiz2_question_and_answer_3, quiz2_question_and_answer_4,  quiz2_question_and_answer_5,
                        quiz2_question_and_answer_6, quiz2_question_and_answer_7, quiz2_question_and_answer_8,
                        quiz2_question_and_answer_9,  quiz2_question_and_answer_10,
                        quiz2_question_and_answer_1, quiz2_question_and_answer_2,
                        quiz2_question_and_answer_3, quiz2_question_and_answer_4, quiz2_question_and_answer_5,
                        quiz2_question_and_answer_6, quiz2_question_and_answer_7, quiz2_question_and_answer_8,
                        quiz2_question_and_answer_9, quiz2_question_and_answer_10,
                        quiz3_question_and_answer_1, quiz3_question_and_answer_2,
                        quiz3_question_and_answer_3, quiz3_question_and_answer_4, quiz3_question_and_answer_5,
                        quiz3_question_and_answer_6, quiz3_question_and_answer_7, quiz3_question_and_answer_8,
                        quiz3_question_and_answer_9, quiz3_question_and_answer_10])
    db.session.commit()

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
        self.password = hash_pwd(password)
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
