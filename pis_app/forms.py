"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
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