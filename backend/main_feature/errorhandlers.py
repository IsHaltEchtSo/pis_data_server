from .controller import main_blueprint

from flask import render_template



@main_blueprint.errorhandler(404)
def not_found(e):
    return render_template('main/404.jinja2', data={'e':e})