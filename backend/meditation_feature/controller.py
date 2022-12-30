from .models import Meditation
from .forms import MeditationForm

from flask import render_template, current_app as app, redirect, url_for



def main():
    db_session = app.get_db_session()
    meditations = db_session.query(Meditation) \
                                .all()
    return render_template('meditation/main.jinja2',
                            data = {'title': 'Routines',
                                    'meditations': meditations})


def meditation_create():
    form = MeditationForm()

    if form.validate_on_submit():
        db_session = app.get_db_session()
        meditation = Meditation( name = form.name.data, 
                                 description = form.description.data )
        db_session.add( meditation )
        db_session.commit()
        return redirect( url_for ( 'meditation_blueprint.main' ) )
    
    return render_template( 'meditation/create.jinja2', 
                            data = { 'title': 'Routines',
                                     'form': form})


    