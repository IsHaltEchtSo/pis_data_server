from .forms import SignupForm
from .models import User

from backend.constants import RolesEnum, FlashEnum

from flask import current_app as app, render_template, flash, redirect, url_for
from flask_login import login_required, current_user, login_user



@login_required
def main():
    if current_user.role == RolesEnum.ADMIN.value:
        db_session = app.DatabaseSession()
        users = db_session.query(User).all()
        return render_template('permissions/main.jinja2', 
                                data = {'title':'Admin Area', 
                                        'RolesEnum': RolesEnum, 
                                        'users': users,
                                        'user': current_user})
    flash(FlashEnum.ADMIN_ERROR.value)
    return redirect(url_for('authentication_blueprint.login'))


def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # User sign up logic upon POST request
        session = app.DatabaseSession()
        existing_user = session \
                            .query(User) \
                            .filter_by(email=form.email.data) \
                            .first()
        if existing_user is None:
            user = User(name=form.name.data, email=form.email.data)
            user.set_password(form.password.data)
            session = app.DatabaseSession()
            session.add(user)
            session.commit()
            login_user(user)
            return redirect(url_for('index_blueprint.main'))

        flash('A User with that email adress already exists!')

    return render_template( 'permissions/signup.jinja2',
                            data={'title':'Create an account.'}, 
                            form=form, 
                            template='sign up page', 
                            body='Sign up for a user account.')