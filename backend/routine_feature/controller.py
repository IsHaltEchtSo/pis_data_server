from flask import Blueprint, render_template



routine_blueprint = Blueprint('routine_blueprint',
                              __name__,
                              template_folder='views')


@routine_blueprint.route('/routine')
def main():
    return render_template('routine/main.jinja2',
                            data = { 'title': 'Routines'})