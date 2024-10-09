from . import users_blueprint
from flask import render_template, redirect, url_for, session, current_app
from .forms import RegForm, RoleForm, StamboekForm, KoppelingenForm
from app import db
from app.models import User
from sqlalchemy.exc import IntegrityError
from app.api import onderwijs_het_archief 

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
            session['registration_email'] = form.username.data
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
    if 'registration_email' not in session:
        # If the session flag is not found, redirect to registration page
        current_app.logger.info('>> session not found, redirecting')
        return redirect(url_for('users.registratie'))
    else:
        form = RoleForm()
        if form.validate_on_submit():
            if form.user_is_teacher.data or form.user_is_student.data:
                # pull the record username from the session
                username = session.get('registration_email')
                if not username:
                    # failsave If no username is found in session, redirect to registration page
                    current_app.logger.info('>> username not found in session, redirecting')
                    return redirect(url_for('users.registratie')) 
                # query the db
                user = User.query.filter_by(username=username).first()
                if form.user_is_teacher.data:
                    user.role_id = 1
                    db.session.commit()
                    # saving role in browser session
                    session['registration_role'] = 1
                    return redirect(url_for('users.stamboeknummer')) 
                else:
                    user.role_id = 2
                    db.session.commit()
                    # saving role in browser session
                    session['registration_role'] = 2  
                    return redirect(url_for('users.mijnkoppelingen')) 
                     
        return render_template('users/rechtenenrollenpagina.html', form=form)
    
@users_blueprint.route('/stamboeknummer', methods=['GET', 'POST'])
def stamboeknummer():    
    form = StamboekForm() 
    if form.validate_on_submit():
        test = onderwijs_het_archief(form.stamboek.data)
        if test == 'OK':
            current_app.logger.info('>> TWERKT')
    return render_template('users/stamboeknummer.html', form=form)

@users_blueprint.route('/mijnkoppelingen', methods=['GET', 'POST'])
def mijnkoppelingen():
    form = KoppelingenForm()  
    return render_template('users/mijnkoppelingen.html', form=form) 