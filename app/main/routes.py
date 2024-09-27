from flask import render_template
from . import main

@main.route('/')
def index():
    """
    Renders the homepage.

    :return: Rendered template for the homepage 
    """
    return render_template('index.html')

