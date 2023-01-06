from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email       = StringField(  label='Email',
                                validators=[Email(message='Enter a valid email.'),
                                            DataRequired()])

    password    = PasswordField(label='Password', 
                                validators=[DataRequired()])

    submit      = SubmitField(label='Log In')