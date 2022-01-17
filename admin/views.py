from flask_login import login_required, current_user
from flask import Blueprint, render_template
from sqlalchemy import desc
from app import requires_roles
from models import User, Quiz


admin_blueprint = Blueprint('admin', __name__, template_folder='templates')


@admin_blueprint.route('/admin')
@login_required
@requires_roles('admin')
def admin():
    return render_template("admin.html")


@admin_blueprint.route('/view_reported_quizzes')
@login_required
@requires_roles('admin')
def view_reported_quizzes():
    reported_quizzes = Quiz.query.filter(Quiz.user_id != current_user.id, Quiz.number_of_reports > 0).order_by(desc('number_of_reports')).all()
    return render_template('admin.html', quizzes=reported_quizzes)


@admin_blueprint.route('/view_users', methods=['GET', 'POST'])
@requires_roles('admin')
def view_users():
    current_users = User.query.filter_by(role='user').all()
    return render_template('admin.html', users=current_users)


@admin_blueprint.route('/logs', methods=['GET', 'POST'])
@requires_roles('admin')
def logs():
    with open("admin.log", "r") as f:
        content = f.read().splitlines()[-10:]
        content.reverse()

    return render_template('admin.html', logs=content)
