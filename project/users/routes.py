from . import users_blueprint
from flask import current_app, render_template, redirect, url_for, make_response, request
from .forms import RegForm

@users_blueprint.route('/registratie', methods=['GET', 'POST'])
def registratie():
    """
    Renders the registration page.

    :return: Rendered template for the registration page.
    """
    form = RegForm()
    if form.validate_on_submit():  # Checks if the form was submitted and passed all validations
        # Process the form data
        pass  # Placeholder for further processing (like saving the data)
    else:  # If the form was not valid
        # Loop through each field that has errors
        for field, errors in form.errors.items():
        # Loop through each error message for the current field
            for error in errors:
            # Print the error message for debugging
                print(f"Error in {field}: {error}") 
    return render_template('users/registratiepagina.html', form=form)