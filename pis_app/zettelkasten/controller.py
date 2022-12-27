from .models import Zettel
from .forms import ZettelEditForm, ZettelSearchForm, ZettelCreateForm
from .utility import ZettelFactory, DBSessionProcessor
from pis_app.constants import RolesEnum, FlashEnum

from flask import Blueprint, current_app as app, render_template, abort, flash, redirect, url_for
from flask_login import current_user, login_required




zk_bp = Blueprint('zk_bp',
                  __name__,
                  template_folder='views')


# Route for 'Zettel' page
@zk_bp.route('/zettel-view/<string:luhmann_id>')
def zettel_view(luhmann_id):
    db_session = app.get_db_session()
    zettel = db_session.query(Zettel) \
                        .filter(Zettel.luhmann_id == luhmann_id).one() 
    if not zettel:
        abort(404)

    return render_template('zettelkasten/zettel-view.html', 
                            context={'title': zettel.title, 
                                     'zettel':zettel, 
                                     'RolesEnum': RolesEnum})


# Route for 'Zettel Search' page
@zk_bp.route('/zettel-search', 
            methods=['POST', 'GET'])
def zettel_search():
    form = ZettelSearchForm()

    if form.validate_on_submit():
        db_session = app.get_db_session()
        zettels = db_session.query(Zettel) \
                                .filter(
                                    Zettel.title.contains(form.title.data), 
                                    Zettel.luhmann_id.contains(form.luhmann_id.data))

        return render_template('zettelkasten/zettel-search.html', 
                                context={'title': 'Zettel Search', 
                                         'zettels':zettels, 
                                         'form':form})
    
    return render_template('zettelkasten/zettel-search.html', 
                            context={'title': 'Zettel Search',
                                     'form': form})


# Route for 'Label Zettel' page
@zk_bp.route('/zettel-create', 
            methods=['POST', 'GET'])
def zettel_create():
    form = ZettelCreateForm()

    if form.validate_on_submit():
        db_session = app.get_db_session()
        zettel = ZettelFactory(form=form, db_session=db_session) \
                    .create_zettel()
        processor = DBSessionProcessor(db_session=db_session)

        if not processor.confirm_constraint_satisfaction(object=zettel):
            flash(FlashEnum.ZETTELDUPLICATE.value)
            return redirect(url_for('zk_bp.zettel_create'))

        processor.add_to_db(zettel)

        return redirect(url_for('zk_bp.zettel_view', 
                                luhmann_id=zettel.luhmann_id))

    return render_template('zettelkasten/zettel-create.html', 
                            context={'title': 'Label Zettel', 
                                     'form': form})


# Route for 'Zettel Edit' page
@zk_bp.route('/zettel-edit/<string:luhmann_id>', 
            methods=['POST', 'GET'])
def zettel_edit(luhmann_id):
    db_session = app.get_db_session()
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
            return redirect(url_for('zk_bp.zettel_edit', 
                                    luhmann_id=luhmann_id))
        
        processor.add_to_db(updated_zettel)

        return redirect(url_for('zk_bp.zettel_view', 
                                luhmann_id=updated_zettel.luhmann_id))

    return render_template('zettelkasten/zettel-edit.html', 
                            context={'title': 'Zettel Edit', 
                                     'zettel':zettel, 
                                     'form':form})


@zk_bp.route('/zettel-delete/<string:luhmann_id>')
@login_required
def zettel_delete(luhmann_id):
    db_session = app.get_db_session()
    zettel = db_session.query(Zettel) \
                        .filter(Zettel.luhmann_id == luhmann_id).one()

    if not zettel or not (current_user.role == RolesEnum.ADMIN.value):
        abort(404)
    
    DBSessionProcessor(db_session=db_session) \
        .delete_from_db(zettel)
    flash(f"[{zettel.luhmann_id} {zettel.title}] was deleted")
    return redirect(url_for('index'))