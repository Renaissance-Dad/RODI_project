import pytest
from app import create_app
from project.users.forms import RegForm

@pytest.fixture
def app():
    """
    Create the Flask app for testing with the testing configuration.
    """
    app = create_app('testing')

    with app.app_context():  # Set the app context for the test
        yield app  # This provides the app to the tests

@pytest.fixture
def client(app):
    """
    Set up the Flask test client for use in tests.
    """
    # `app` fixture is passed as an argument to create the test client
    with app.test_client() as client:
        yield client  # Provide the test client to tests

@pytest.fixture
def form(app):
    with app.app_context():  # Ensure app context is set
        yield RegForm()  # Provide the initialized form to tests