from .forms import MeditationForm, MeditationEditForm
from .models import Meditation
from .utility import MeditationFactory, DatabaseSessionProcessor

from backend.constants import RolesEnum

from flask import render_template, current_app as app, redirect, url_for, abort, flash
from flask_login import current_user



def main():
    meditations = app.DatabaseSession().query(Meditation) \
                                       .all()
    return render_template('meditation/main.jinja2',
                            data = {'title': 'Routines',
                                    'meditations': meditations})


def create():
    form = MeditationForm()

    if form.validate_on_submit():
        database_session = app.DatabaseSession()
        meditation = Meditation( name = form.name.data, 
                                 description = form.description.data )
        database_session.add( meditation )
        database_session.commit()
        return redirect( url_for ( 'meditation_blueprint.main' ) )
    
    return render_template( 'meditation/create.jinja2', 
                            data = { 'title': 'Routines',
                                     'form': form})


def view(meditation_id):
    meditation = app.DatabaseSession().query(Meditation) \
                                      .filter(Meditation.id == meditation_id) \
                                      .one() 
    if not meditation:
        abort(404)

    return render_template('meditation/view.jinja2', 
                            data = {'title': 'Meditation', 
                                    'meditation': meditation, 
                                    'RolesEnum': RolesEnum})


def edit(meditation_id):
    database_session = app.DatabaseSession()
    meditation = database_session.query(Meditation) \
                                 .filter(Meditation.id == meditation_id) \
                                 .one()
                        
    if not meditation or not (current_user.role == RolesEnum.ADMIN.value):
        abort(404)
    
    form = MeditationEditForm()

    if form.validate_on_submit():
        updated_meditation = MeditationFactory(form = form, 
                                               database_session = database_session) \
                                .update_meditation(meditation = meditation)

        DatabaseSessionProcessor(database_session = database_session) \
            .add_to_database(updated_meditation)

        return redirect( url_for( 'meditation_blueprint.view', 
                                   meditation_id = updated_meditation.id ) )

    return render_template('meditation/edit.jinja2', 
                            data = {'title': 'Meditation', 
                                    'meditation': meditation, 
                                    'form': form             } )


def delete(meditation_id):
    database_session = app.DatabaseSession()
    meditation = database_session.query(Meditation) \
                                 .filter(Meditation.id == meditation_id) \
                                 .one()

    if not meditation or not (current_user.role == RolesEnum.ADMIN.value):
        abort(404)
    
    DatabaseSessionProcessor(database_session=database_session) \
        .delete_from_database(meditation)

    return redirect(url_for('meditation_blueprint.main'))

    