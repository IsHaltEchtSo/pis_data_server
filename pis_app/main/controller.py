from pis_app.constants import RolesEnum

from flask import Blueprint, render_template



main_bp = Blueprint('main_bp',
                    __name__,
                    template_folder='views')


@main_bp.route('/')
@main_bp.route('/index')
def index():
    return render_template('main/index.html', 
                            context={'title': 'Index', 
                                     'RolesEnum': RolesEnum})