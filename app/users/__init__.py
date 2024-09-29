"""
The blueprint handles everything related to the users
"""
from flask import Blueprint
from pathlib import Path

# Determine the absolute path to the templates folder
template_path = Path(__file__).parent / 'templates'

users_blueprint = Blueprint('users', __name__, template_folder=str(template_path))


from . import routes
from . import forms