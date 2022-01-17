import pytest
from app import app
from models import User
from flask_login import LoginManager, login_user


def app_config():
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False


def register_blueprints():
    from quiz.views import quiz_blueprint
    from users.views import users_blueprint

    app.register_blueprint(users_blueprint)
    app.register_blueprint(quiz_blueprint)


def setup_login_manager():
    # LOGIN MANAGER
    login_manager = LoginManager()
    login_manager.login_view = 'users.login'
    login_manager.init_app(app)  # login manager is registered with testing app

    from models import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


@pytest.fixture
def client():

    # set application configuration for testing
    app_config()
    # register blueprints
    register_blueprints()
    setup_login_manager()

    return app.test_client()






