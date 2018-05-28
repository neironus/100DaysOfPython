from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators
from wtforms.widgets import HiddenInput


class AddForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    submit = SubmitField('Add')


class EditForm(AddForm):
    id = IntegerField(widget=HiddenInput())
    submit = SubmitField('Edit')
