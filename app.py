"""
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public Licensealong with this program. If not, see <https://www.gnu.org/licenses/>.
"""

from flask import Flask, render_template, url_for, request, make_response, redirect

app = Flask(__name__)

# Import the blueprints
from project.cookies import cookies_blueprint

# Register the blueprints
app.register_blueprint(cookies_blueprint)


@app.route('/')
def index():
    """
    Renders the homepage.

    Retrieves the cookie value from the user's browser and passes it to the 
    template to display relevant content.

    :return: Rendered template for the homepage with the cookie value.
    """
    cookie_value = request.cookies.get('cookies_avr')
    return render_template('index.html', cookie_value=cookie_value)


