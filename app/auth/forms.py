from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import Email, Length

class LoginForm(FlaskForm):
    username = StringField('Jouw E-mailadres', 
        render_kw={"id": "myEmail", "autocomplete":"username"}, 
        validators=[
            Length(max=50, message="E-mailadres niet langer dan 50 tekens."),
            Email(message="Ongeldig E-mailadres.")
        ])
    userpasw = PasswordField('Jouw wachtwoord', 
        render_kw={"autocomplete": "current-password", "id": "myPasw"
        })
    forgetmenot = BooleanField('Ingelogd blijven')
    loginsubmit = SubmitField('INLOGGEN', 
        render_kw={"id": "mySubmit"
        })