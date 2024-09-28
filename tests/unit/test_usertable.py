import pytest
from flask import Flask
from wtforms import ValidationError

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User object is created
    THEN check the email is valid and hashed password does not equal the password provided
    """
    return 
