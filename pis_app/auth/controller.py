from .models import LoginForm, SignupForm, User
from .utility import *
from flask import Blueprint, redirect, url_for, current_app as app, flash, render_template
from flask_login import current_user, logout_user, login_user, LoginManager



auth_bp = Blueprint(    'auth_bp',
                        __name__,
                        template_folder='views')


@auth_bp.route('/signup', methods=['POST', 'GET'])
def signup():
    """
    User sign-up page.

    GET requests serve the sign up page.
    POST requests validate input data & create user account.
    """
    form = SignupForm()
    if form.validate_on_submit():
        # User sign up logic upon POST request
        session = app.get_db_session()
        existing_user = session \
                            .query(User) \
                            .filter_by(email=form.email.data) \
                            .first()
        if existing_user is None:
            user = User(name=form.name.data, email=form.email.data)
            user.set_password(form.password.data)
            session = app.get_db_session()
            session.add(user)
            session.commit()
            login_user(user)
            return redirect(url_for('index'))

        flash('A User with that email adress already exists!')

    return render_template( 'auth/signup.html',
                            context={'title':'Create an account.'}, 
                            form=form, 
                            template='sign up page', 
                            body='Sign up for a user account.')


@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    """
    Login page for registered users.
    
    GET requests serve the log in page
    POST requests validate input data & log in the user
    """
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        session = app.get_db_session()
        user = session \
                .query(User) \
                .filter_by(email=form.email.data) \
                .first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            user.set_last_login()
            return redirect(url_for('index'))
        flash('Invalid usernamed/password combination')
        return redirect(url_for('auth_bp.login'))
    
    return render_template( 'auth/login.html',
                            form=form,
                            context={'title':'Log in.'},
                            template='login-page',
                            body='Log in with your user account.')


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))