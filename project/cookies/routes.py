from . import cookies_blueprint
from flask import current_app, render_template, redirect, url_for, make_response, request

@cookies_blueprint.route('/accept_all_cookies')
def accept_all_cookies():
    """
    This function/route creates a response that sets a cookie named 'cookies_avr' 
    with the value 'all' for one year. The cookie is available site-wide. 
    After setting the cookie, it redirects the user back to the page where the route was triggered.

    :return: Redirect response with the 'cookies_avr' cookie set to 'all'.
    """
    # Create a response and redirect to the previous page
    referrer = request.referrer or url_for('index')  # If no referrer, fall back to index

    # Create a response to set the cookie
    response = make_response(redirect(referrer))
    
    # Set a cookie named 'cookies_avr' with value 'all' and a max age of 1 year
    response.set_cookie('cookies_avr', 'all', path='/', max_age=60*60*24*365)
    
    # Redirect back to the original page (index)
    return response

@cookies_blueprint.route('/accept_necessary_cookies')
def accept_necessary_cookies():
    """
    This function/route creates a response that sets a cookie named 'cookies_avr' 
    with the value 'mandatory' for one year. The cookie is available site-wide. 
    After setting the cookie, it redirects the user back to the page where the route was triggered.

    :return: Redirect response with the 'cookies_avr' cookie set to 'mandatory'.
    """
    # Create a response and redirect to the previous page
    referrer = request.referrer or url_for('index')  # If no referrer, fall back to index

    # Create a response to set the cookie
    response = make_response(redirect(referrer))
    
    # Set a cookie named 'cookies_avr' with value 'mandatory' and a max age of 1 year
    response.set_cookie('cookies_avr', 'mandatory', path='/', max_age=60*60*24*365)
    
    # Redirect back to the original page (index)
    return response

@cookies_blueprint.route('/cookiebeleid')
def cookiebeleid():
    """
    Renders the cookiebeleid information page.

    :return: Rendered template for cookiebeleid page.
    """
    cookie_value = request.cookies.get('cookies_avr')
    return render_template('cookies/cookiebeleid.html', cookie_value=cookie_value)