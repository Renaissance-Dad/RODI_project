"""
The blueprint handles everything related to the authorization of users.
Flask-login extension is extensively used.
"""
from flask import Blueprint
from pathlib import Path

# Determine the absolute path to the templates folder
template_path = Path(__file__).parent / 'templates'

# Create the blueprint and set the template folder
auth_blueprint = Blueprint('auth', __name__, template_folder=str(template_path))

from . import routes