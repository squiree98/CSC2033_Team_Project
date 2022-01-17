from flask_login import login_user, logout_user, login_required, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db, requires_roles
from models import User, Score
from users.forms import RegisterForm, LoginForm
from datetime import datetime
import bcrypt

users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # check if form questions are answered correctly
    counter = 0
    if form.q1.data == "TRUE":
        counter = counter + 1
    if form.q2.data == "FALSE":
        counter = counter + 1
    if form.q3.data == "TRUE":
        counter = counter + 1
    if form.q4.data == "FALSE":
        counter = counter + 1
    if form.q5.data == "TRUE":
        counter = counter + 1
    if form.validate_on_submit():
        if counter != 5:
            flash('Questions have not been answered correctly')
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('Username address already exists')
            return render_template('register.html', form=form)
        email_address = form.email.data
        username = email_address.split('@', 1)[0]

        new_user = User(username=username, email=form.email.data, password=form.password.data, role='user',
                        subscribed=0)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("users.login"))

    return render_template('register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        pwd_in = form.password.data.encode()

        if not user or not bcrypt.checkpw(pwd_in, user.password):
            flash('Please check your login details and try again.')
            return render_template('login.html', form=form)
        login_user(user)
        user.currently_logged_in = datetime.now()
        user.last_logged_in = user.currently_logged_in
        db.session.add(user)
        db.session.commit()

        if current_user.role == 'user':
            return redirect(url_for('users.profile'))
        else:
            return redirect(url_for('quiz.quizzes'))

    return render_template('login.html', form=form)


@users_blueprint.route('/profile')
@login_required
@requires_roles('user')
def profile():

    # get score objects for currently logged-in user
    scores = Score.query.filter_by(user_id=current_user.id).all()
    total_score = 0

    for score in scores:
        total_score += score.score_value

    return render_template('profile.html', score=total_score)


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))