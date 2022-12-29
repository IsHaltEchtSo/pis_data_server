from backend.auth_feature.models import User
from backend.constants import RolesEnum, FlashEnum

from flask import Blueprint, current_app as app, render_template, flash, redirect, url_for
from flask_login import login_required, current_user



admin_blueprint = Blueprint('admin_blueprint',
                            __name__,
                            template_folder='views')


@admin_blueprint.route('/admin')
@login_required
def dashboard():
    if current_user.role == RolesEnum.ADMIN.value:
        db_session = app.get_db_session()
        users = db_session.query(User).all()
        return render_template('admin/dashboard.jinja2', 
                                data={'title':'Admin Area', 
                                         'RolesEnum': RolesEnum, 
                                         'users':users,
                                         'user': current_user,})
    flash(FlashEnum.ADMIN_ERROR.value)
    return redirect(url_for('main_blueprint.index'))