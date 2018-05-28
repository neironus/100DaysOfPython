from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, \
    validators, widgets
from wtforms.widgets import HiddenInput
from wtforms.ext.sqlalchemy.fields import QuerySelectField, \
    QuerySelectMultipleField

from models import Day, Party


class MultiCheckboxField(QuerySelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


def list_days():
    return Day.query


def list_parties():
    return Party.query


class AddForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    day_id = QuerySelectField('Day', query_factory=list_days, get_label='name')
    submit = SubmitField('Add')


class EditForm(AddForm):
    id = IntegerField(widget=HiddenInput())
    submit = SubmitField('Edit')


class RecommendationsForm(FlaskForm):
    id = IntegerField(widget=HiddenInput())
    # recommendations = MultiCheckboxField(
    #     'Party', query_factory=list_parties, get_label='name'
    # )
    party_ids = QuerySelectMultipleField('Party', query_factory=list_parties, get_label='name')
    submit = SubmitField('Edit')


