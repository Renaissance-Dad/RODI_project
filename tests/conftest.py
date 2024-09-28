import pytest
from app import create_app, db
from project.users.forms import RegForm

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
    with app.app_context():  # Ensure app context is set
        yield RegForm()  # Provide the initialized form to tests


@pytest.fixture
def init_database(app):
    with app.app_context():
        # Create a user instance
        user = db.User(email='benweyts@email.com', password='rodi123')
        # Add the user to the session
        db.session.add(user)
        # Commit the session to save the user in the database
        db.session.commit()
        # Return the user instance for use in tests
        yield user
        # cleanup when done
        db.session.remove()