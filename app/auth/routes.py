from . import auth_blueprint 
from flask import current_app, render_template, redirect, url_for, make_response, request

@auth_blueprint.route('/login')
def login():
    """
    This function/route logs a user in.

    :return: Redirect response with a logged-in user.
    """
    
    # Redirect back ?
    return "logged in"