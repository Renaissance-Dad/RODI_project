import pytest
from app import create_app, db
from app.users.forms import RegForm

@pytest.fixture
def app():
    """
    Create the Flask app for testing with the testing configuration.
    """
    app = create_app('testing')

    with app.app_context():  # Set the app context for the test
        
        db.create_all() #create the db tables
        yield app  # This provides the app to the tests
        
        db.drop_all() #Clean up after testing

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
    with app.test_request_context('/'):
        yield RegForm()  # Provide the initialized form to tests
