from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import Email, Length

class RegForm(FlaskForm):
    username = StringField('Jouw E-mailadres', 
        render_kw={"id": "myEmail"}, 
        validators=[
            Length(max=50, message="E-mailadres niet langer dan 50 tekens."),
            Email(message="Ongeldig E-mailadres.")
        ])
    userpasw = PasswordField('Jouw wachtwoord', 
        render_kw={"autocomplete": "new-password", "id": "myPasw"
        })
    usersubmit = SubmitField('NIEUW ACCOUNT AANMAKEN*', 
        render_kw={"id": "mySubmit"
        })
    
class RoleForm(FlaskForm):
    user_is_teacher = SubmitField('Leerkracht',
        render_kw={"id": "iamTeacher"
        })
    user_is_student = SubmitField('Leerling',
           render_kw={"id": "iamStudent"
        })
    