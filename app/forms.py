from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired, ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User, Tune

class TuneForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    composer = StringField('Composer', validators=[DataRequired()])
    key = StringField('Key')
    other_key = StringField('Other Keys')
    song_form = StringField('Form')
    style = StringField('Style')
    meter = IntegerField('Meter')
    year = IntegerField('Year')
    decade = StringField('Decade')
    knowledge = RadioField('Knowledge', choices=["Know", "Learning", "Don't Know"])
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    search_term = StringField('Search Term')
    submit = SubmitField('Search')