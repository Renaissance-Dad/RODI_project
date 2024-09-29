"""
This .py contains all the model class definitions for the app. We use SQLAlchemy in combination with postgreSQL 
"""
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True) 
    password_hash = db.Column(db.String(256))  # Use String for storing hashed passwords

    @property
    def password(self):
        raise AttributeError('Alle wachtwoorden worden geëncrypteerd.')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username