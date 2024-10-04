"""
This .py contains all the model class definitions for the app. We use SQLAlchemy in combination with postgreSQL 
"""
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True) 
    password_hash = db.Column(db.String(256))  # Use String for storing hashed passwords
    
    # Foreign key to the roles table
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) 

    # One-to-many relationship with OAuth (one user can have many oauth providers)
    oauth_accounts = db.relationship('OAuthAccount', back_populates='user', cascade="all, delete-orphan")

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
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    
    # One-to-many relationship with users table (many users, each one role) 
    users = db.relationship('User', backref='role') 

    def __repr__(self):
        return '<Role %r>' % self.name

class OAuthAccount(db.Model):
    __tablename__ = 'oauth_accounts'
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(50), nullable=False)  # e.g., 'google', 'smartschool'
    provider_user_id = db.Column(db.String(200), nullable=False)  # User ID from the OAuth provider
    access_token = db.Column(db.String(500), nullable=False)
    refresh_token = db.Column(db.String(500), nullable=True)
    expires_at = db.Column(db.Integer, nullable=True)  # Timestamp of token expiration in seconds
    
    # Foreign key to the User table
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Reference to the User object
    user = db.relationship('User', back_populates='oauth_accounts')
    
    def __repr__(self):
        return f'<OAuthAccount {self.provider} for User {self.user_id}>'
