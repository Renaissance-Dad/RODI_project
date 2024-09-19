"""
The blueprint handles everything related to the cookies.
Specifically, it sets the avr cookie and also contains the cookiepolicy and the cookieconfigurator form.
"""
from flask import Blueprint

cookies_blueprint = Blueprint('cookies', __name__, template_folder='templates')

from . import routes