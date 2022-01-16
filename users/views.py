from flask_login import login_user, logout_user, login_required
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db
from models import User
from users.forms import RegisterForm, LoginForm
from datetime import datetime
import bcrypt

users_blueprint = Blueprint('users', __name__, template_folder='templates')


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('Username address already exists')
            return render_template('register.html', form=form)
        emailadress = form.email.data
        username = emailadress.split('@', 1)[0]

        new_user = User(username=username, email=form.email.data, password=form.password.data, role='user',
                        subscribed=0)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        pwdin = form.password.data.encode()
        dbhash = user.password

        if not user or not bcrypt.checkpw(pwdin, dbhash):
            flash('Please check your login details and try again')
            return render_template('login.html', form=form)
        login_user(user)
        user.currently_logged_in = datetime.now()
        user.last_logged_in = user.currently_logged_in
        db.session.add(user)
        db.session.commit()
        return render_template('profile.html')
    return render_template('login.html', form=form)


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))