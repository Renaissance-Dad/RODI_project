import pytest
from flask import Flask
from project.cookies import cookies_blueprint
from project.users import users_blueprint
from project.users.forms import RegForm
from config import TestingConfig


import sys
import os




@pytest.fixture(scope='module')
def app():
    """
    Create the Flask app for testing with the testing configuration.
    """
    sys.path.append(os.path.dirname(__file__))

    app = Flask(__name__)
    

    app.config.from_object(TestingConfig)  # Use TestingConfig directly

    app.register_blueprint(cookies_blueprint)
    app.register_blueprint(users_blueprint)

    with app.app_context():  # Set the app context for the test
        yield app  # This provides the app to the tests

@pytest.fixture(scope='module')
def client(app):
    """
    Set up the Flask test client for use in tests.
    """
    # `app` fixture is passed as an argument to create the test client
    with app.test_client() as client:
        yield client  # Provide the test client to tests

@pytest.fixture
def form(client):
    return RegForm()