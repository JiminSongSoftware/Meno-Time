import flask 
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail, Message

basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "jimin.song.software@gmail.com"
app.config['MAIL_PASSWORD'] = "hnmciiausvxmlvhr"
app.config["MAIL_USE_TLS"] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

app.config.from_mapping(
        SECRET_KEY = 'it-dont-matter',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False

)

db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

from myapp import routes, models
