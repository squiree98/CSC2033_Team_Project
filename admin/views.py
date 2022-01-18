from flask_login import login_required, current_user
from flask import Blueprint, render_template
from sqlalchemy import desc
from app import requires_roles
from models import User, Quiz

# Create the admin blueprint
admin_blueprint = Blueprint('admin', __name__, template_folder='templates')


@admin_blueprint.route('/admin')
@login_required
@requires_roles('admin')
def admin():
    """
    Renders the default admin page
    :return users:
    author Oscar
    date 11/01/2022
    """
    # Placeholder array to prevent an error caused when admin.html tries to render without a valid array
    placeholder_users = [1]
    return render_template("admin.html", users=placeholder_users)


@admin_blueprint.route('/view_reported_quizzes')
@login_required
@requires_roles('admin')
def view_reported_quizzes():
    """
        Displays all reported quizzes on the Admin page
        :return quizzes:
        author Oscar
        date 12/01/2022
    """
    # Get a list of reported quizzes from the Quiz table (all quizzes with a number of reports greater than 0)
    reported_quizzes = Quiz.query.filter(Quiz.user_id != current_user.id, Quiz.number_of_reports > 0).order_by(desc('number_of_reports')).all()
    return render_template('admin.html', quizzes=reported_quizzes)


@admin_blueprint.route('/view_users', methods=['GET', 'POST'])
@requires_roles('admin')
def view_users():
    """
        Displays all users currently logged in
        :return users:
        author Oscar
        date 12/01/2022
    """
    # Get a list of all online users (where there last login date is the same as their current login date)
    online_users = User.query.filter_by(role='user').where(User.last_logged_in == User.currently_logged_in).all()
    return render_template('admin.html', users=online_users)


@admin_blueprint.route('/logs', methods=['GET', 'POST'])
@requires_roles('admin')
def logs():
    """
        Displays logs from log file on admin page
        :return logs:
        author Oscar
        date 12/01/2022
    """
    # Open admin.log file as read only
    with open("admin.log", "r") as f:
        # Read the last 10 lines from the log file
        content = f.read().splitlines()[-10:]
        content.reverse()

    return render_template('admin.html', logs=content)
