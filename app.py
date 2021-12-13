from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# CONFIG
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://csc2033_team27:Lobe?CamJest@cs-db.ncl.ac.uk:3306/csc2033_team27'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'csc2033_team27_key'


db = SQLAlchemy(app)


# HOME PAGE VIEW
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':

    from quiz.views import quiz_blueprint

    app.register_blueprint(quiz_blueprint)

    app.run(debug=True)
