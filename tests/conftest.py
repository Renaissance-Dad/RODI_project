
import pytest
from flask import Flask
from app import cookies_blueprint, users_blueprint

@pytest.fixture(scope='module')
def client():
    """
    This fixture sets up the Flask application, attaches the blueprint,
    and provides a test client for use in the tests.
    """
    app = Flask(__name__)
    app.register_blueprint(cookies_blueprint)
    app.register_blueprint(users_blueprint)
    app.config['TESTING'] = True

    @cookies

    # Establish an application context before running the tests.
    with app.test_client() as client:
        yield client