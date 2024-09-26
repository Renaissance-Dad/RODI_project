from datetime import datetime

def test_footer_links(client):
    """Test that footer links work correctly."""
    # Test the cookie policy link
    response = client.get('/cookiebeleid') 
    assert response.status_code == 200  # Ensure it returns a valid response

    # Test the GitHub link
    assert b'https://github.com/Renaissance-Dad/RODI_project' in response.data


def test_footer_datetime(client):
    """Test that the correct year is displayed in the copyright notice"""
    current_year = datetime.now().year

    # Test the footer
    response = client.get('/')

    # Assert that the response data contains the copyright year
    assert f'&copy; Toets en Feedback Vlaanderen VZW - {current_year}'.encode() in response.data
