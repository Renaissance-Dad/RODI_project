from . import cookies_blueprint
from flask import current_app, render_template, redirect, url_for, make_response

@cookies_blueprint.route('/accept_all_cookies')
def accept_all_cookies():
    """
    This function/route creates a response that sets a cookie named 'cookies_avr' 
    with the value 'all' for one year. After setting the cookie, it redirects
    the user back to the homepage.

    :return: Redirect response to the homepage with the 'cookies_avr' cookie set to 'all'.
    """
    # Create a response to set the cookie
    response = make_response(redirect(url_for('index')))
    
    # Set a cookie named 'cookies_avr' with value 'all' and a max age of 1 year
    response.set_cookie('cookies_avr', 'all', max_age=60*60*24*365)
    
    # Redirect back to the original page (index)
    return response

@cookies_blueprint.route('/accept_necessary_cookies')
def accept_necessary_cookies():
    """
    This function/route creates a response that sets a cookie named 'cookies_avr' 
    with the value 'mandatory' for one year. After setting the cookie, it 
    redirects the user back to the homepage.

    :return: Redirect response to the homepage with the 'cookies_avr' cookie set to 'mandatory'.
    """
    # Create a response to set the cookie
    response = make_response(redirect(url_for('index')))
    
    # Set a cookie named 'cookies_avr' with value 'mandatory' and a max age of 1 year
    response.set_cookie('cookies_avr', 'mandatory', max_age=60*60*24*365)
    
    # Redirect back to the original page (index)
    return response

@cookies_blueprint.route('/cookiebeleid')
def cookiebeleid():
    """
    Renders the cookiebeleid information page.

    :return: Rendered template for cookiebeleid page.
    """
    return render_template('cookies/cookiebeleid.html')