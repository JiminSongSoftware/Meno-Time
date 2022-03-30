import flask 
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail, Message

basedir = os.path.abspath(os.path.dirname(__file__))

application = flask.Flask(__name__)

application.config['MAIL_SERVER'] = 'smtp.gmail.com'
application.config['MAIL_PORT'] = 465
application.config['MAIL_USERNAME'] = "jimin.song.software@gmail.com"
application.config['MAIL_PASSWORD'] = "hnmciiausvxmlvhr"
application.config["MAIL_USE_TLS"] = False
application.config['MAIL_USE_SSL'] = True

mail = Mail(application)

application.config.from_mapping(
        SECRET_KEY = 'it-dont-matter',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False

)

db = SQLAlchemy(application)
login = LoginManager(application)
login.login_view = 'login'

from myapp import routes, models
