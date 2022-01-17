from flask_login import login_user, logout_user, login_required, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db, requires_roles
from models import User
from users.forms import RegisterForm, LoginForm
from datetime import datetime

admin_blueprint = Blueprint('admin', __name__, template_folder='templates')


@admin_blueprint.route('/admin')
@login_required
@requires_roles('admin')
def admin():
    return render_template("admin.html")


@admin_blueprint.route('/view_reported_quizzes',  methods=['GET', 'POST'])
@login_required
@requires_roles('admin')
def view_reported_quizzes():
    return render_template("admin.html")


@admin_blueprint.route('/view_users', methods=['POST'])
@login_required
@requires_roles('admin')
def view_users():
    return render_template('admin.html', current_users=User.query.filter_by(role='user').all())


@admin_blueprint.route('/logs', methods=['POST'])
@login_required
@requires_roles('admin')
def logs():
    with open("lottery.log", "r") as f:
        content = f.read().splitlines()[-10:]
        content.reverse()

    return render_template('admin.html', logs=content, name=current_user.firstname)