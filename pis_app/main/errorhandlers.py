from .controller import main_bp

from flask import render_template



@main_bp.errorhandler(404)
def not_found(e):
    return render_template('main/404.html', context={'e':e})