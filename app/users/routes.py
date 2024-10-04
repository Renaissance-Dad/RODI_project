from . import users_blueprint
from flask import render_template, redirect, url_for, session, current_app
from .forms import RegForm, RoleForm
from app import db
from app.models import User
from sqlalchemy.exc import IntegrityError

@users_blueprint.route('/registratie', methods=['GET', 'POST'])
def registratie():
    """
    Renders the registration page.

    :return: Rendered template for the registration page.
    """
    form = RegForm()
    if form.validate_on_submit():  # Checks if the form was submitted and passed all validations
        try:
            new_user = User(username=form.username.data, password=form.userpasw.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('users.rechtenenrollen'))
        except IntegrityError:
            db.session.rollback()
            form.username.errors.append("E-mailadres reeds geregistreerd.")
    else:  # If the form was not valid
        # Loop through each field that has errors
        for field, errors in form.errors.items():
        # Loop through each error message for the current field
            for error in errors:
            # Print the error message for debugging
                print(f"Error in {field}: {error}") 
    return render_template('users/registratiepagina.html', form=form)

@users_blueprint.route('/wachtwoordvergeten')
def wachtwoordvergeten():
    return "PLACEHOLDER WACHTWOORDVERGETEN"

@users_blueprint.route('/rechtenenrollen', methods=['GET', 'POST'])
def rechtenenrollen():
    if 'completed_registration' not in session:
        # If the session flag is not found, redirect to registration page
        current_app.logger.info('>> session not found, redirecting')
        return redirect(url_for('users.registratie'))
    else:
        form = RoleForm()
        if form.validate_on_submit():
            if form.user_is_teacher.data:
                return "PLACEHOLDER"
            elif form.user_is_student.data:
                return "PLACEHOLDER"
        return render_template('users/rechtenenrollenpagina.html', form=form)