from pis_app.constants import RolesEnum
from pis_app.database import Base

import datetime as dt
from flask_login import UserMixin
from flask_wtf import FlaskForm
from sqlalchemy import Column, Integer, String,DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo



class User(UserMixin, Base):
    """A dummy model just yet"""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(12), nullable=False, unique=False)
    email = Column(String(40), unique=True, nullable=False)
    role = Column(Integer, default=RolesEnum.USER.value)
    password = Column(String(200), primary_key=False, unique=False, nullable=False)
    created_on = Column(DateTime, index=False, unique=False, nullable=True)
    last_login = Column(DateTime, index=False, unique=False, nullable=True)

    def __init__(self, name: str, email) -> None:
        self.name       = name
        self.email      = email
        self.created_on = dt.datetime.now()
        self.last_login = dt.datetime.now()
        self.role       = RolesEnum.USER.value

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash( password,
                                                method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def set_last_login(self):
        """Update the last_login attribute"""
        self.last_login = dt.datetime.now()


    def __repr__(self) -> str:
        return f"<User {self.name}>"


class LoginForm(FlaskForm):
    """User Log-in Form."""
    email       = StringField(  label='Email',
                                validators=[Email(message='Enter a valid email.'),
                                            DataRequired()])

    password    = PasswordField(label='Password', 
                                validators=[DataRequired()])

    submit      = SubmitField(label='Log In')


class SignupForm(FlaskForm):
    """User Sign-up Form."""
    name = StringField(
        'Name',
        validators=[
            DataRequired(),
            Length(max=12)])
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
            DataRequired()])
    submit = SubmitField(label='Register')