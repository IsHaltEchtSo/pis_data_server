from .forms import LoginForm
from .utility import *

from ..permissions.models import User

from flask import redirect, url_for, current_app as app, flash, render_template
from flask_login import current_user, logout_user, login_user, LoginManager



def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = app.DatabaseSession().query(User) \
                                   .filter_by(email = form.email.data) \
                                   .first()

        if user and user.check_password(password = form.password.data):
            login_user(user)
            user.set_last_login()
            return redirect(url_for('index_blueprint.main'))
        
        flash('Invalid usernamed/password combination')
        
        return redirect(url_for('authentication_blueprint.login'))
    
    return render_template( 'authentication/login.jinja2',
                            form=form,
                            data={'title':'Log in.'},
                            template='login-page',
                            body='Log in with your user account.')


def logout():
    logout_user()
    return redirect(url_for('index_blueprint.main'))