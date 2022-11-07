"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length
)


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Name',
        validators=[
            DataRequired(),
            Length(max=12)
        ]
    )
    email = StringField(
        label='Email',
        validators=[
            Length(min=6),
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    password = PasswordField(
        label='Password',
        validators=[
            Length(min=6, message='Select a stronger password.'),
            DataRequired()
        ]
    )
    confirm = PasswordField(
        label='Confirm Your Password',
        validators=[
            EqualTo('password', message='Passwords must match.'),
            DataRequired()
        ]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email = StringField(
        label='Email',
        validators=[
            Email(message='Enter a valid email.'),
            DataRequired()
        ]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class ZettelSearchForm(FlaskForm):
    """ZettelSearch Form"""
    luhmann_identifier = StringField(
        label='Luhmann ID',
    )
    title = StringField(
        label='Title'
    )
    submit = SubmitField('Search')


class ZettelEditForm(FlaskForm):
    """Form to edit Zettel"""
    luhmann_identifier = StringField(
        label='Luhmann ID'
    )
    title = StringField(
        label='Title',
    )
    content = TextAreaField(
        label='Content'
    )
    links = StringField(
        label="Links"
    )
    backlinks = StringField(
        label="Backlinks"
    )
    submit = SubmitField('Save')


class DigitaliseZettelForm(FlaskForm):
    """Form to capture data for new Zettels"""
    luhmann_identifier = StringField(
        label='Luhmann ID',
        validators=[
            DataRequired()
        ]
    )
    title = StringField(
        label='Title',
        validators=[
            DataRequired()
        ]
    )
    content = TextAreaField(
        label='Content'
    )
    links = StringField(
        label='Links'
    )
    backlinks = StringField(
        label='Backlinks'
    )
    submit = SubmitField('Save')

