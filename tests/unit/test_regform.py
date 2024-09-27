import pytest
from flask import Flask
from wtforms import ValidationError
from project.users.forms import RegForm  

def test_username_field_valid_email(form):
    """
    This test checks if a valid email is correctly validated in the form class.
    """
    # Given a valid email
    form_data = {'username': 'validemail@example.com', 'userpasw': 'mypassword'}

    # Create an instance of RegForm using the valid form data
    form = RegForm(data=form_data)

    # Assert that the form passes validation
    assert form.validate() is True