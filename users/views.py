from flask import Blueprint, render_template, request, flash
from app import db
from models import User
from users.forms import RegisterForm, LoginForm

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

        return render_template('login.html', form=form)

    return render_template('register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return render_template('profile.html')
    return render_template('login.html', form=form)
