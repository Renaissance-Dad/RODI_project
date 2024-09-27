def test_accept_all_cookies(client):
    """
    This test checks if the '/accept_all_cookies' route sets the 'cookies_avr' cookie 
    to 'all' and redirects to the referrer or index.
    """
    # Simulate a request with a referrer
    response = client.get('/accept_all_cookies', headers={'Referer': '/somepage'})
    
    # Assert the cookie is correctly set
    assert response.status_code == 302  # Redirection
    assert 'cookies_avr' in response.headers['Set-Cookie']
    assert 'all' in response.headers['Set-Cookie']
    
    # Check that it redirects to the correct referrer
    assert response.location == '/somepage'

def test_accept_all_cookies_no_referrer(client):
    """
    This test checks if the '/accept_all_cookies' route redirects to the index 
    when there's no referrer.

    THERE ARE SOME ISSUES WITH THE PATHS
    """
    # Simulate a request without a referrer
    response = client.get('/accept_all_cookies', headers={'Referer': ''})
    
    # Assert the cookie is correctly set
    assert response.status_code == 302  # Redirection
    assert 'cookies_avr' in response.headers['Set-Cookie']
    assert 'all' in response.headers['Set-Cookie']
    
    # Check that it redirects to the index
    assert response.location == '/'

def test_accept_necessary_cookies(client):
    """
    This test checks if the '/accept_necessary_cookies' route sets the 'cookies_avr' cookie 
    to 'mandatory' and redirects to the referrer.
    """
    # Simulate a request with a referrer
    response = client.get('/accept_necessary_cookies', headers={'Referer': '/somepage'})
    
    # Assert the cookie is correctly set
    assert response.status_code == 302  # Redirection
    assert 'cookies_avr' in response.headers['Set-Cookie']
    assert 'mandatory' in response.headers['Set-Cookie']
    
    # Check that it redirects to the correct referrer
    assert response.location == '/somepage'

def test_accept_necessary_cookies_no_referrer(client):
    """
    This test checks if the '/accept_necessary_cookies' route redirects with a 302

    """
    # Simulate a request without a referrer
    response = client.get('/accept_necessary_cookies', headers={'Referer': ''})
    
    # Assert the cookie is correctly set
    assert response.status_code == 302  # Redirection
    assert 'cookies_avr' in response.headers['Set-Cookie']
    assert 'mandatory' in response.headers['Set-Cookie']

def test_cookiebeleid_with_cookie(client):
    """
    This test checks if the '/cookiebeleid' route renders the cookiebeleid page 
    """
    # Simulate a request with the 'cookies_avr' cookie set to 'all'
    response = client.get('/cookiebeleid', headers={'Cookie': 'cookies_avr=all'})
    
    # Assert the page renders successfully
    assert response.status_code == 200