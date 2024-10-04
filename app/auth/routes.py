from . import auth_blueprint 
from .forms import LoginForm
from flask import current_app, render_template, redirect, url_for, make_response, request

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """
    This function/route logs a user in.

    :return: Redirect response with a logged-in user.
    """
    form = LoginForm()
    # Redirect back ?
    return render_template('auth/login.html', form=form)
