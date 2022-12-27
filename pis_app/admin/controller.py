from pis_app.auth.models import User
from pis_app.constants import RolesEnum, FlashEnum

from flask import Blueprint, current_app as app, render_template, flash, redirect, url_for
from flask_login import login_required, current_user



admin_bp = Blueprint('admin_bp',
                     __name__,
                     template_folder='views')


@admin_bp.route('/admin')
@login_required
def admin_dashboard():
    if current_user.role == RolesEnum.ADMIN.value:
        db_session = app.get_db_session()
        users = db_session.query(User).all()
        return render_template('admin/main.html', 
                                context={'title':'Admin Area', 
                                         'RolesEnum': RolesEnum, 
                                         'users':users,
                                         'user': current_user,})
    flash(FlashEnum.ADMIN_ERROR.value)
    return redirect(url_for('index'))