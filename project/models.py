from myapp import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from project import login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128), unique=True)
    password  = db.Column(db.String(128))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

class FlashCard(db.Model):
    title = db.Column(db.String(64), unique =True, index-True)
    body = db.Column(db.String(256))
    
    def __repr__(self):
        return f'<{self.title}>'

class Notes(db.Model):
    title = db.Column(db.String, unique=True, index=True)
    
    def __repr__(self):
	return f'<Note: {self.title}>'
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
