def get_form_html(form):
    html = ''
    for field in form:
        html += str(field.label) + str(field())

    return html