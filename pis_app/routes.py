"""
See 'rsc/Redirect_Backbone.png' for a diagram of the endpoints.
"""
from flask import render_template, current_app as app, redirect, flash, url_for
from flask_login import login_required, current_user
from .auth.models import User
from .constants import RolesEnum, FlashEnum
import datetime as dt
import pis_app.errorhandlers


# Route for 'Home' page
@app.route('/')
@app.route('/index')
def index():
    return render_template('views/index.html', 
                            context={'title': 'Index', 
                                     'RolesEnum': RolesEnum})


# Route for 'Admin' page
@app.route('/admin')
@login_required
def admin():
    if current_user.role == RolesEnum.ADMIN.value:
        db_session = app.get_db_session()
        users = db_session.query(User).all()
        return render_template('views/admin.html', 
                                context={'title':'Admin Area', 
                                         'RolesEnum': RolesEnum, 
                                         'users':users,
                                         'user': current_user,})
    flash(FlashEnum.ADMIN_ERROR.value)
    return redirect(url_for('index'))