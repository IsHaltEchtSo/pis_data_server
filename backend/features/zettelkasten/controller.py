from .forms import ZettelEditForm, ZettelSearchForm, ZettelCreateForm
from .models import Zettel
from .utility import ZettelFactory, DBSessionProcessor

from backend.constants import RolesEnum, FlashEnum

from flask import current_app as app, render_template, abort, flash, redirect, url_for
from flask_login import current_user, login_required



def main():
    return render_template( 'zettelkasten/main.jinja2',
                             data = { 'feature_title': 'Zettelkasten',
                                      'feature_url': url_for( 'zettelkasten_blueprint.main' ) } )


def view(luhmann_id):
    db_session = app.DatabaseSession()
    zettel = db_session.query(Zettel) \
                        .filter(Zettel.luhmann_id == luhmann_id).one() 
    if not zettel:
        abort(404)

    return render_template( 'zettelkasten/view.jinja2', 
                            data = { 'feature_title': 'Zettelkasten',
                                     'feature_url': url_for( 'zettelkasten_blueprint.main' ),
                                     'zettel':zettel, 
                                     'RolesEnum': RolesEnum } )


def search():
    form = ZettelSearchForm()

    if form.validate_on_submit():
        db_session = app.DatabaseSession()
        zettels = db_session.query(Zettel) \
                                .filter(
                                    Zettel.title.contains(form.title.data), 
                                    Zettel.luhmann_id.contains(form.luhmann_id.data))

        return render_template( 'zettelkasten/search.jinja2', 
                                data = { 'feature_title': 'Zettelkasten',
                                         'feature_url': url_for( 'zettelkasten_blueprint.main' ),
                                         'zettels':zettels, 
                                         'form':form } )
    
    return render_template('zettelkasten/search.jinja2', 
                            data = { 'feature_title': 'Zettelkasten',
                                     'feature_url': url_for( 'zettelkasten_blueprint.main' ),
                                     'form': form})


def create():
    form = ZettelCreateForm()

    if form.validate_on_submit():
        db_session = app.DatabaseSession()
        zettel = ZettelFactory(form=form, db_session=db_session) \
                    .create_zettel()
        processor = DBSessionProcessor(db_session=db_session)

        if not processor.confirm_constraint_satisfaction(object=zettel):
            flash(FlashEnum.ZETTELDUPLICATE.value)
            return redirect(url_for('zettelkasten_blueprint.create'))

        processor.add_to_database(zettel)

        return redirect(url_for('zettelkasten_blueprint.view', 
                                luhmann_id=zettel.luhmann_id))

    return render_template('zettelkasten/create.jinja2', 
                            data = { 'feature_title': 'Zettelkasten',
                                     'feature_url': url_for( 'zettelkasten_blueprint.main' ), 
                                     'form': form})


def edit(luhmann_id):
    db_session = app.DatabaseSession()
    zettel = db_session.query(Zettel) \
                        .filter(Zettel.luhmann_id == luhmann_id) \
                        .scalar()
                        
    if not zettel or not (current_user.role == RolesEnum.ADMIN.value):
        abort(404)
    
    form = ZettelEditForm()

    if form.validate_on_submit():
        updated_zettel = ZettelFactory(form=form, db_session=db_session) \
                            .update_zettel(zettel=zettel)
        processor = DBSessionProcessor(db_session=db_session)

        if not processor.confirm_constraint_satisfaction(object=updated_zettel):
            flash(FlashEnum.ZETTELDUPLICATE.value)
            return redirect( url_for('zettelkasten_blueprint.edit', 
                                     luhmann_id=luhmann_id ) )
        
        processor.add_to_database(updated_zettel)

        return redirect(url_for('zettelkasten_blueprint.view', 
                                luhmann_id=updated_zettel.luhmann_id ) )

    return render_template('zettelkasten/edit.jinja2', 
                            data = { 'feature_title': 'Zettelkasten',
                                     'feature_url': url_for( 'zettelkasten_blueprint.main' ), 
                                     'zettel':zettel, 
                                     'form':form } )


@login_required
def delete(luhmann_id):
    db_session = app.DatabaseSession()
    zettel = db_session.query(Zettel) \
                        .filter(Zettel.luhmann_id == luhmann_id).one()

    if not zettel or not (current_user.role == RolesEnum.ADMIN.value):
        abort(404)
    
    DBSessionProcessor(db_session=db_session) \
        .delete_from_database(zettel)
    flash(f"[{zettel.luhmann_id} {zettel.title}] was deleted")
    return redirect(url_for('zettelkasten_blueprint.main'))


def gallery():
    db_session = app.DatabaseSession()
    zettels = db_session.query(Zettel) \
                            .all()
    return render_template('zettelkasten/gallery.jinja2',
                            data = { 'feature_url': url_for('zettelkasten_blueprint.main'),
                                     'feature_title': 'Zettelkasten',
                                     'zettels': zettels})