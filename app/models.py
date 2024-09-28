"""
This .py contains all the model class definitions for the app. We use SQLAlchemy in combination with postgreSQL 
"""
from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True) 
    password = db.Column(db.String(128))  # Use String for storing hashed passwords

    def __repr__(self):
        return '<User %r>' % self.username