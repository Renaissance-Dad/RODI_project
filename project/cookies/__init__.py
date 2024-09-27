"""
The blueprint handles everything related to the cookies.
Specifically, it sets the avr cookie and also contains the cookiepolicy and the cookieconfigurator form.
"""
from flask import Blueprint
from pathlib import Path

# Determine the absolute path to the templates folder
template_path = Path(__file__).parent / 'templates'

# Create the blueprint and set the template folder
cookies_blueprint = Blueprint('cookies', __name__, template_folder=str(template_path))

from . import routes