from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# CONFIG
app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://csc2033_team27:Lobe?CamJest@cs-db.ncl.ac.uk:3306/csc2033_team27'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'csc2033_team27_key'

db = SQLAlchemy(app)


# HOME PAGE VIEW
@app.route('/')
def index():
    return render_template('index.html')


def register():
    return render_template('register.html')


def login():
    return render_template('login.html')


if __name__ == '__main__':

    login_manager = LoginManager()
    login_manager.login_view = 'users.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    #blueprints
    from users.views import users_blueprint
    app.register_blueprint(users_blueprint)

    app.run(debug=True)
