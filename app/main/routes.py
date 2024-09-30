from flask import render_template
from . import main

@main.route('/')
def index():
    """
    Renders the homepage.

    :return: Rendered template for the homepage 
    """
    return render_template('index.html')

@main.route('/EULA')
def EULA():
    return "EULA PLACEHOLDER"

@main.route('/GPL3_0')
def GPL3_0():
    return "OPEN SOURCE PLACEHOLDER"

@main.route('/toegankelijkheidsverklaring')
def toegankelijkheidsverklaring():
    return "toegeankelijkheidsverklaring placeholder"