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
    """
    # Simulate a request without a referrer
    response = client.get('/accept_all_cookies')
    
    # Assert the cookie is correctly set
    assert response.status_code == 302  # Redirection
    assert 'cookies_avr' in response.headers['Set-Cookie']
    assert 'all' in response.headers['Set-Cookie']
    
    # Check that it redirects to the index
    assert response.location == '/'

def test_accept_necessary_cookies(client):
    """
    This test checks if the '/accept_necessary_cookies' route sets the 'cookies_avr' cookie 
    to 'mandatory' and redirects to the referrer or index.
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
    This test checks if the '/accept_necessary_cookies' route redirects to the index 
    when there's no referrer.
    """
    # Simulate a request without a referrer
    response = client.get('/accept_necessary_cookies')
    
    # Assert the cookie is correctly set
    assert response.status_code == 302  # Redirection
    assert 'cookies_avr' in response.headers['Set-Cookie']
    assert 'mandatory' in response.headers['Set-Cookie']
    
    # Check that it redirects to the index
    assert response.location == '/'

def test_cookiebeleid_no_cookie(client):
    """
    This test checks if the '/cookiebeleid' route renders the cookiebeleid page 
    and passes None as cookie_value when the 'cookies_avr' cookie is not set.
    """
    # Simulate a request with no 'cookies_avr' cookie
    response = client.get('/cookiebeleid')
    
    # Assert the page renders successfully
    assert response.status_code == 200
    assert b'cookiebeleid' in response.data  # Check if the template renders (based on content in HTML)

def test_cookiebeleid_with_cookie(client):
    """
    This test checks if the '/cookiebeleid' route renders the cookiebeleid page 
    and passes the value of 'cookies_avr' when the cookie is set.
    """
    # Simulate a request with the 'cookies_avr' cookie set to 'all'
    response = client.get('/cookiebeleid', headers={'Cookie': 'cookies_avr=all'})
    
    # Assert the page renders successfully
    assert response.status_code == 200
    assert b'cookiebeleid' in response.data  # Check if the template renders (based on content in HTML)