from .forms import MeditationForm, MeditationEditForm
from .models import Meditation
from .utility import MeditationFactory, DBSessionProcessor

from backend.constants import RolesEnum

from flask import render_template, current_app as app, redirect, url_for, abort, flash
from flask_login import current_user



def main():
    db_session = app.get_db_session()
    meditations = db_session.query(Meditation) \
                                .all()
    return render_template('meditation/main.jinja2',
                            data = {'title': 'Routines',
                                    'meditations': meditations})


def create():
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


def view(meditation_id):
    db_session = app.get_db_session()
    meditation = db_session.query(Meditation) \
                        .filter(Meditation.id == meditation_id).one() 
    if not meditation:
        abort(404)

    return render_template('meditation/view.jinja2', 
                            data = {'title': 'Meditation', 
                                    'meditation': meditation, 
                                    'RolesEnum': RolesEnum})


def edit(meditation_id):
    db_session = app.get_db_session()
    meditation = db_session.query(Meditation) \
                        .filter(Meditation.id == meditation_id) \
                        .one()
                        
    if not meditation or not (current_user.role == RolesEnum.ADMIN.value):
        abort(404)
    
    form = MeditationEditForm()

    if form.validate_on_submit():
        updated_meditation = MeditationFactory(form = form, 
                                               db_session = db_session) \
                                .update_meditation(meditation = meditation)

        processor = DBSessionProcessor(db_session = db_session)
        processor.add_to_db(updated_meditation)

        return redirect( url_for( 'meditation_blueprint.view', 
                                   meditation_id = updated_meditation.id ) )

    return render_template('meditation/edit.jinja2', 
                            data = {'title': 'Meditation', 
                                    'meditation': meditation, 
                                    'form': form             } )


def delete(meditation_id):
    db_session = app.get_db_session()
    meditation = db_session.query(Meditation) \
                        .filter(Meditation.id == meditation_id) \
                        .one()

    if not meditation or not (current_user.role == RolesEnum.ADMIN.value):
        abort(404)
    
    DBSessionProcessor(db_session=db_session) \
        .delete_from_db(meditation)
    
    flash(f"[{meditation.name}] was deleted")

    return redirect(url_for('meditation_blueprint.main'))

    