from app import app as flask_app
import pytest

@pytest.fixture
def app():
    """
    This fixture creates and configures a new app instance for each test.
    """
    # Set up the app for testing
    flask_app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
    return flask_app

@pytest.fixture
def client(app):
    """
    This fixture provides a test client for the application.
    """
    # Use the app context to avoid needing to push context in each test
    with app.test_client() as client:
        with app.app_context():
            yield client