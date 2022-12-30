from .forms import RoutineForm
from .models import Routine

from flask import Blueprint, render_template, current_app as app, redirect, url_for



routine_blueprint = Blueprint('routine_blueprint',
                              __name__,
                              template_folder='views')


@routine_blueprint.route( '/routine')
def main():
    db_session = app.get_db_session()
    routines = db_session.query(Routine) \
                            .all()
    return render_template('routine/main.jinja2',
                            data = { 'title': 'Routines',
                                     'routines': routines})


@routine_blueprint.route( '/routine-create',
                          methods = ['GET', 'POST'])
def routine_create():
    form = RoutineForm()

    if form.validate_on_submit():
        db_session = app.get_db_session()
        routine = Routine( name = form.name.data, 
                           starttime = form.starttime.data )
        db_session.add(routine)
        db_session.commit()
        return redirect( url_for ( 'routine_blueprint.main' ) )
    
    return render_template('routine/routine-create.jinja2', 
                            data={'title': 'Routines',
                                  'form': form})