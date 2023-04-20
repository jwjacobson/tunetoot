from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SubmitField, IntegerField, RadioField, PasswordField, BooleanField
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
    # knowledge = RadioField('Knowledge', choices=["Know", "Learning", "Don't Know"])
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    search_term = StringField('Universal Search')
    submit = SubmitField('Search')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('An account with that username already exists')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('An account with that email address already exists ')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')