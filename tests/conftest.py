import pytest
from app import app, db
from flask_login import LoginManager
from models import User, Quiz


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


@pytest.fixture(scope='function')
def init_database(client):
    # Create the database and the database table
    db.create_all()

    user = User(username="User", email="User@email.com", password="password123", role="user", subscribed=False)
    db.session.add(user)
    db.session.commit()

    quiz = Quiz(user.id, "Climate Action", "5-12")
    db.session.add(quiz)
    db.session.commit()

    yield

    # Delete the database tables
    db.drop_all()


@pytest.fixture(scope='function')
def login_default_user(client):
    client.post('/login',
                     data=dict(email='User@email.com', password='password123'),
                     follow_redirects=True)

    yield

    # log out user
    client.get('/logout', follow_redirects=True)




