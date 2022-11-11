"""
See 'rsc/Redirect_Backbone.png' for a diagram of the endpoints.
"""
#TODO: CUD operations make a new Zettel Update
from flask import render_template, current_app as app, redirect, flash, url_for, abort
from flask_login import login_required, current_user
from .models import User, Zettel
from .constants import RolesEnum, FlashEnum
from .forms import ZettelSearchForm, ZettelEditForm, DigitaliseZettelForm
import datetime as dt
from sqlalchemy.exc import IntegrityError
from .app import cache
import pis_app.errorhandlers
from .utility import ZettelFactory, CacheProcessor


# Route for 'Home' page
@app.route('/')
@app.route('/index')
def index_view():
    return render_template('views/index.html', 
                            context={'title': 'Index', 
                                    'RolesEnum': RolesEnum})


# Route for 'History' page
@app.route('/history')
def history_view():
    return render_template('views/history.html', 
                            context={'title': 'History'})


# Route for 'Manual' page
@app.route('/manual')
def manual_view():
    return render_template('views/manual.html', 
                            context={'title': 'Manual'})


# Route for 'Zettel Search' page
@app.route('/zettel_search', methods=['POST', 'GET'])
def zettel_search_view():

    form = ZettelSearchForm()
    if form.validate_on_submit():
        db_session = app.get_db_session()
        zettels = db_session.query(Zettel) \
                                .filter(
                                    Zettel.title.contains(form.title.data), 
                                    Zettel.luhmann_id.contains(form.luhmann_id.data))
        return render_template('views/zettel_search.html', 
                                context={'title': 'Zettel Search', 
                                        'zettels':zettels, 
                                        'form':form})
    
    return render_template('views/zettel_search.html', 
                            context={'title': 'Zettel Search',
                                    'form': form})


# Route for 'Zettel' page
@app.route('/zettel/<string:luhmann_id>')
def zettel_view(luhmann_id):
    db_session = app.get_db_session()
    zettel = db_session.query(Zettel).filter(Zettel.luhmann_id == luhmann_id).one()
    if zettel:
        return render_template('views/zettel.html', 
                                context={'title': zettel.title, 
                                        'zettel':zettel, 
                                        'RolesEnum': RolesEnum})
    abort(404)


# Route for 'Zettel Edit' page
@app.route('/zettel_edit/<string:luhmann_id>', methods=['POST', 'GET'])
def zettel_edit_view(luhmann_id):
    db_session = app.get_db_session()
    zettel = db_session.query(Zettel).filter(Zettel.luhmann_id == luhmann_id).scalar()

    if not zettel:
        abort(404)
    
    form = ZettelEditForm()
    if form.validate_on_submit():

        updated_zettel = ZettelFactory(form=form, db_session=db_session) \
                            .update_zettel(zettel=zettel)

            flash(FlashEnum.ZETTELDUPLICATE.value)
            return redirect(url_for('zettel_edit_view', 
                                    luhmann_id=luhmann_id))

    return render_template('views/zettel_edit.html', 
                            context={'title': 'Zettel Edit', 
                                    'zettel':zettel, 
                                    'form':form})


# Route for 'Checklist' page
@app.route('/checklist')
def checklist_view():
    return render_template('views/checklist.html', 
                            context={'title': 'Checklist'})


# Route for 'Digitalize Zettel' page
@app.route('/digitalize_zettel')
def digitalize_zettel_view():
    return render_template('views/digitalize_zettel.html', 
                            context={'title': 'Digitalize Zettel'})


# Route for 'Label Zettel' page
@app.route('/label_zettel', methods=['POST', 'GET'])
def label_zettel_view():
    form = DigitaliseZettelForm()
    if form.validate_on_submit():
        db_session = app.get_db_session()

        zettel = ZettelFactory(form=form, db_session=db_session).create_zettel()

            flash(FlashEnum.ZETTELDUPLICATE.value)
            return redirect(url_for('label_zettel_view'))

    return render_template('views/label_zettel.html', 
                            context={'title': 'Label Zettel', 
                                    'form': form})


# Route for 'Success' page
@app.route('/success')
def success_view():
    return render_template('views/success.html', 
                            context={'title': 'Success'})


# Route for 'Admin' page
@app.route('/admin')
@login_required
def admin_view():
    if current_user.role == RolesEnum.ADMIN.value:
        db_session = app.get_db_session()
        users = db_session.query(User).all()
        return render_template('views/admin.html', 
                                context={'title':'Admin Area', 
                                        'RolesEnum': RolesEnum, 
                                        'users':users})
    flash(FlashEnum.ADMIN_ERROR.value)
    return redirect(url_for('index_view'))


@app.route('/bottleneck')
# @cache.cached()  # caches the WHOLE view
def bottleneck_view():
    app.logger.info(f'Time upon request: {dt.datetime.now()}')
    title = CacheProcessor(cache=cache) \
                .get(keyword='title')
    app.logger.info(f'Time upon response: {dt.datetime.now()}')
    return render_template('views/bottleneck.html', 
                            context={'title':title})


@app.route('/delete/<string:luhmann_id>')
@login_required
def delete_zettel(luhmann_id):
    db_session = app.get_db_session()
    zettel = db_session.query(Zettel) \
                        .filter(Zettel.luhmann_id == luhmann_id).one()
    if zettel:
        db_session.delete(zettel)
        db_session.commit()
        flash(f"[{zettel.luhmann_id} {zettel.title}] was deleted")
        return redirect(url_for('index_view'))
    abort(404)