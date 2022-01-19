from functools import wraps
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from newsapi import NewsApiClient
from flask_login import LoginManager, current_user
from flask_share import Share

import logging

# create share object
share = Share()


# LOGGING
class SecurityFilter(logging.Filter):
    def filter(self, record):
        return "SECURITY" in record.getMessage()


# writes logs to admin.log file
fh = logging.FileHandler('admin.log', 'w')
fh.setLevel(logging.WARNING)
fh.addFilter(SecurityFilter())
formatter = logging.Formatter('%(asctime)s : %(message)s', '%d/%m/%Y %I:%M:%S %p')
fh.setFormatter(formatter)

logger = logging.getLogger('')
logger.propagate = False
logger.addHandler(fh)

# CONFIG
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://csc2033_team27:Lobe?CamJest@cs-db.ncl.ac.uk:3306/csc2033_team27'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'csc2033_team27_key'

share.init_app(app)
db = SQLAlchemy(app)


def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                # Redirect the user to an unauthorised notice!
                return render_template('403.html')
            return f(*args, **kwargs)
        return wrapped
    return wrapper


# HOME PAGE VIEW
@app.route('/')
def index():
    """
    author Matt
    date 19/01/2022
    """
    # retrieves data from the news api key
    newsapi = NewsApiClient(api_key="c56ddcf9b5104c0289b116ed7aac8d16")
    # retrieves all news articles from bbc-news to do with climate change
    topheadlines = newsapi.get_everything(sources="bbc-news", q="climate change")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []
    # creates a list for each news article which contains the title, description, url and image
    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        url.append(myarticles['url'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, url, img)

    return render_template('index.html', context=mylist)


# ERROR PAGE VIEWS
@app.errorhandler(403)
def page_forbidden(error):
    """
    in case of 403 error redirects to relevant page
    author Bogdan
    date 15/01/2021
    """
    return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(error):
    """
    in case of 404 error redirects to relevant page
    author Bogdan
    date 15/01/2021
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """
    in case of 500 error redirects to relevant page
    author Bogdan
    date 15/01/2021
    """
    return render_template('500.html'), 500


if __name__ == '__main__':
    # BLUEPRINTS
    from users.views import users_blueprint
    from quiz.views import quiz_blueprint
    from admin.views import admin_blueprint

    app.register_blueprint(users_blueprint)
    app.register_blueprint(quiz_blueprint)
    app.register_blueprint(admin_blueprint)

    # LOGIN MANAGER
    login_manager = LoginManager()
    login_manager.login_view = 'users.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    app.run(debug=True)
