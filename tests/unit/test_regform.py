from project.users.forms import RegForm
from tests.unit.helpers import get_form_html

def test_email_validation(form):
    """Test that the email field correctly validates email addresses."""
    form = RegForm(username='invalid-email', userpasw='password123')
    assert not form.validate(), "Form should not validate with invalid email"

    form.username.data = 'validemail@example.com'
    assert form.validate(), "Form should validate with a correct email format"

def test_email_max_length(form):
    """Test that the email field does not accept more than 50 characters."""
    long_email = 'a' * 39 + '@example.com'  # 51 characters
    form = RegForm(username=long_email, userpasw='password123')
    assert not form.validate(), "Form should not validate with an email longer than 50 characters"
        
    valid_length_email = 'a' * 38 + '@example.com'  # 50 characters
    form.username.data = valid_length_email
    assert form.validate(), "Form should validate with an email of 50 or fewer characters"

def test_password_field_attribute_exists(form):
    """Test that the password field exists and renders correctly."""
    form = RegForm()     
    assert 'autocomplete="new-password"' in str(form.userpasw), "Password field should have the correct autocomplete attribute"
    assert 'id="myPasw"' in str(form.userpasw), "Password field should have the correct id"

def test_submit_field_attribute_exists(form):
    """Test that the submit field exists and renders correctly."""
    form = RegForm()
    assert 'id="mySubmit"' in str(form.usersubmit), "Submit button should have the correct id"
    assert 'NIEUW ACCOUNT AANMAKEN*' in str(form.usersubmit), "Submit button should have the correct label"

def test_form_rendering(form):
    """Test that the form renders the expected HTML."""
    form = RegForm()  # Initialize the form
    form_html = get_form_html(form)
    assert 'id=&#34;myEmail&#34;' in str(form_html), "The form should include the email field with the correct id"
    assert 'id=&#34;mySubmit&#34;' in str(form_html), "The form should include the submit field with the correct id"
    assert 'id=&#34;myPasw&#34;' in str(form_html), "The form should include the pasw field with the correct id"