from flask import current_app as app, render_template, request, redirect, flash, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from .forms import SignupForm, LoginForm
from .models import User
from .app import login_manager


@app.route('/login', methods=['POST', 'GET'])
def login_view():
    """
    Login page for registered users.
    
    GET requests serve the log in page
    POST requests validate input data & log in the user
    """
    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('index_view'))

    form = LoginForm()
    if form.validate_on_submit():
        session = app.get_db_session()
        user = session.query(User).filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            user.set_last_login()
            return redirect(url_for('index_view'))
        flash('Invalid usernamed/password combination')
        return redirect(url_for('login_view'))
    
    return render_template(
        'views/login.html',
        form=form,
        context={'title':'Log in.'},
        template='login-page',
        body='Log in with your user account.'
    )


@app.route('/signup', methods=['POST', 'GET'])
def signup_view():
    """
    User sign-up page.

    GET requests serve the sign up page.
    POST requests validate input data & create user account.
    """
    form = SignupForm()
    if form.validate_on_submit():
        # User sign up logic upon POST request
        session = app.get_db_session()
        existing_user = session.query(User).filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(name=form.name.data, email=form.email.data)
            user.set_password(form.password.data)
            session = app.get_db_session()
            session.add(user)
            session.commit()
            login_user(user)
            return redirect(url_for('index_view'))

        flash('A User with that email adress already exists!')

    return render_template(
        'views/signup.html',
        context={'title':'Create an account.'}, 
        form=form, 
        template='sign up page', 
        body='Sign up for a user account.'
    )

@app.route('/logout')
def logout_view():
    logout_user()
    return redirect(url_for('index_view'))


@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    "Check if user is logged in on every page load"
    if user_id is not None:
        session = app.get_db_session()
        return session.query(User).get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirected unauthorized user to index view"""
    flash('You must be logged in to be able to access this page')
    return redirect(url_for('index_view'))