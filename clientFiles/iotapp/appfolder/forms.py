from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField, validators
from wtforms.validators import DataRequired

class SubmitForm(FlaskForm):
    filename = StringField('Preferred File Name:', [validators.required(), validators.length(min=1, max=16)])
    submit = SubmitField('Turn on Camera')
