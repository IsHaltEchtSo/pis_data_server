from backend.constants import RolesEnum

from flask import Blueprint, render_template



main_blueprint = Blueprint('main_blueprint',
                           __name__,
                           template_folder='views')


@main_blueprint.route('/')
@main_blueprint.route('/index')
def index():
    return render_template('main/index.jinja2', 
                            data={'title': 'Index', 
                                     'RolesEnum': RolesEnum})