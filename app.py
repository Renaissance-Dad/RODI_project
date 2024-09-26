"""
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public Licensealong with this program. If not, see <https://www.gnu.org/licenses/>.
"""

from flask import Flask, render_template, url_for, request, make_response, redirect
from datetime import datetime

app = Flask(__name__)

# Secret key for WTF forms - generated in flask shell with import secrets, secrets.token_hex((16)
app.config['SECRET_KEY'] = 'ce4ea7ff8704fab7762fae559e4072ba'  

# Import the blueprints
from project.cookies import cookies_blueprint
from project.users import users_blueprint

# Register the blueprints
app.register_blueprint(cookies_blueprint)
app.register_blueprint(users_blueprint)


@app.route('/')
def index():
    """
    Renders the homepage.

    :return: Rendered template for the homepage 
    """
    return render_template('index.html')

@app.context_processor
def inject_year():
    """
    Retrieves the current year.

    This information is used in the copyright notice in the footer.

    :return: Dict with current_year available in all Jinja templates. 

    """
    return dict(current_year=datetime.now().year)

@app.context_processor
def inject_cookies_avr():
    """
    Retrieves the value of the avr cookie

    :return: Dict with cookie_value available in all Jinja templates. 
    """
    cookie_value = request.cookies.get('cookies_avr')
    return dict(cookie_value=cookie_value)

