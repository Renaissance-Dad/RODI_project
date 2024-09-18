'''
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public Licensealong with this program. If not, see <https://www.gnu.org/licenses/>.
'''

from flask import Flask, render_template, url_for, request, make_response, redirect

app = Flask(__name__)


@app.route('/')
def index():
    cookie_value = request.cookies.get('cookies_avr')
    return render_template('index.html', cookie_value=cookie_value)

@app.route('/accept_all_cookies')
def accept_all_cookies():
    # Create a response to set the cookie
    response = make_response(redirect(url_for('index')))
    
    # Set a cookie named 'cookies_avr' with value 'all' and a max age of 1 year
    response.set_cookie('cookies_avr', 'all', max_age=60*60*24*365)
    
    # Redirect back to the original page (index)
    return response

@app.route('/accept_necessary_cookies')
def accept_necessary_cookies():
    # Create a response to set the cookie
    response = make_response(redirect(url_for('index')))
    
    # Set a cookie named 'cookies_avr' with value 'mandatory' and a max age of 1 year
    response.set_cookie('cookies_avr', 'mandatory', max_age=60*60*24*365)
    
    # Redirect back to the original page (index)
    return response