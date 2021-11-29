import flask 
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail, Message

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj = flask.Flask(__name__)

myapp_obj.config['MAIL_SERVER'] = 'smtp.gmail.com'
myapp_obj.config['MAIL_PORT'] = 465
myapp_obj.config['MAIL_USERNAME'] = "jimin.song.software@gmail.com"
myapp_obj.config['MAIL_PASSWORD'] = "hnmciiausvxmlvhr"
myapp_obj.config["MAIL_USE_TLS"] = False
myapp_obj.config['MAIL_USE_SSL'] = True

mail = Mail(myapp_obj)

myapp_obj.config.from_mapping(
        SECRET_KEY = 'it-dont-matter',
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False

)

db = SQLAlchemy(myapp_obj)
login = LoginManager(myapp_obj)
login.login_view = 'login'

from myapp import routes, models
