from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField,\
    validators
from wtforms.widgets import HiddenInput
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from days.models import Day


def list_days():
    return Day.query


class AddForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    # day = SelectField('Day', coerce=int, choices=days)
    day = QuerySelectField('Day', query_factory=list_days, get_label='name')
    submit = SubmitField('Add')


class EditForm(AddForm):
    id = IntegerField(widget=HiddenInput())
    submit = SubmitField('Edit')
