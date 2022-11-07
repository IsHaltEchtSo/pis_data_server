"""
See 'rsc/Redirect_Backbone.png' for a diagram of the endpoints.
"""
#TODO: CUD operations make a new Zettel Update
from flask import render_template, current_app as app, redirect, flash, url_for
from flask_login import login_required, current_user
from .models import RolesEnum, User, Zettel
from .app import cache
from .forms import ZettelSearchForm, ZettelEditForm, DigitaliseZettelForm
import time
import datetime as dt
from sqlalchemy.exc import IntegrityError
import uuid



# Route for 'Home' page
@app.route('/')
@app.route('/index')
def index_view():
    return render_template('views/index.html', context={'title': 'Index', 'RolesEnum': RolesEnum})


# Route for 'History' page
@app.route('/history')
def history_view():
    return render_template('views/history.html', context={'title': 'History'})


# Route for 'Manual' page
@app.route('/manual')
def manual_view():
    return render_template('views/manual.html', context={'title': 'Manual'})


# Route for 'Zettel Search' page
@app.route('/zettel_search', methods=['POST', 'GET'])
def zettel_search_view():
    zettels = []

    form = ZettelSearchForm()
    if form.validate_on_submit():
        session = app.Session()
        if form.luhmann_identifier.data and form.title.data:
            zettels = session.query(Zettel).filter(Zettel.title.contains(form.title.data), Zettel.luhmann_identifier.contains(form.luhmann_identifier.data))
        elif form.luhmann_identifier.data:
            zettels = session.query(Zettel).filter(Zettel.luhmann_identifier.contains(form.luhmann_identifier.data))
        elif form.title.data:
            zettels = session.query(Zettel).filter(Zettel.title.contains(form.title.data))
        else:
            zettels = session.query(Zettel).all()
        return render_template('views/zettel_search.html', context={'title': 'Zettel Search', 'zettels':zettels, 'form':form})
    
    return render_template('views/zettel_search.html', context={'title': 'Zettel Search', 'zettels':[], 'form':form})


# Route for 'Zettel' page
@app.route('/zettel/<int:zettel_id>')
def zettel_view(zettel_id):
    session = app.Session()
    zettel = session.query(Zettel).get(zettel_id)
    return render_template('views/zettel.html', context={'title': zettel.title, 'zettel':zettel, 'RolesEnum': RolesEnum})


# Route for 'Zettel Edit' page
@app.route('/zettel_edit/<int:zettel_id>', methods=['POST', 'GET'])
def zettel_edit_view(zettel_id):
    session = app.Session()
    zettel = session.query(Zettel).get(zettel_id)
    
    form = ZettelEditForm()
    if form.validate_on_submit():
        zettel_altered = False
        if form.luhmann_identifier.data:
            zettel.luhmann_identifier = form.luhmann_identifier.data
            zettel_altered = True

        if form.title.data:
            zettel.title = form.title.data
            zettel_altered = True
        
        if form.content.data:
            zettel.content = form.content.data
            zettel_altered = True

        if form.links.data:
            link_zettel = session.query(Zettel).filter(Zettel.luhmann_identifier == form.links.data).scalar()
            if link_zettel:
                zettel.links.append(link_zettel)
            else:
                link_zettel = Zettel(luhmann_identifier=form.links.data, title=f"Placeholder Title: <{uuid.uuid4()}>")
                zettel.links.append(link_zettel)
            zettel_altered = True
        
        if form.backlinks.data:
            backlink_zettel = session.query(Zettel).filter(Zettel.luhmann_identifier == form.backlinks.data).scalar()
            if backlink_zettel:
                zettel.backlinks.append(backlink_zettel)
            else: 
                backlink_zettel = Zettel(luhmann_identifier=form.backlinks.data, title=f"Placeholder Title: <{uuid.uuid4()}>")
                zettel.backlinks.append(backlink_zettel)
            zettel_altered = True

        if zettel_altered:
            try:
                session.add(zettel)
                session.commit()
                flash(f'[{zettel.luhmann_identifier}: {zettel.title}] successfully edited!')
                return redirect(url_for('zettel_view', zettel_id=zettel.id))
            except IntegrityError:
                flash("A Zettel with that Title and/or Luhmann ID already exists! Please try again!")
                return redirect(url_for('zettel_edit_view', zettel_id=zettel_id))
        
    return render_template('views/zettel_edit.html', context={'title': 'Zettel Edit', 'zettel':zettel, 'form':form})


# Route for 'Checklist' page
@app.route('/checklist')
def checklist_view():
    return render_template('views/checklist.html', context={'title': 'Checklist'})


# Route for 'Digitalize Zettel' page
@app.route('/digitalize_zettel')
def digitalize_zettel_view():
    return render_template('views/digitalize_zettel.html', context={'title': 'Digitalize Zettel'})


# Route for 'Label Zettel' page
@app.route('/label_zettel', methods=['POST', 'GET'])
def label_zettel_view():
    form = DigitaliseZettelForm()
    if form.validate_on_submit():
        zettel = Zettel(
            luhmann_identifier=form.luhmann_identifier.data,
            title=form.title.data,
            content=form.content.data
        )
        session = app.Session()

        if form.links.data:
            link_zettel = session.query(Zettel).filter(Zettel.luhmann_identifier == form.links.data).scalar()
            if link_zettel:
                zettel.links.append(link_zettel)
            else:
                link_zettel = Zettel(luhmann_identifier=form.links.data, title=f"Placeholder Title: <{uuid.uuid4()}>")
                zettel.links.append(link_zettel)
        
        if form.backlinks.data:
            backlink_zettel = session.query(Zettel).filter(Zettel.luhmann_identifier == form.backlinks.data).scalar()
            if backlink_zettel:
                zettel.backlinks.append(backlink_zettel)
            else: 
                backlink_zettel = Zettel(luhmann_identifier=form.backlinks.data, title=f"Placeholder Title: <{uuid.uuid4()}>")
                zettel.backlinks.append(backlink_zettel)


        try:
            session.add(zettel)
            session.commit()
            return redirect(url_for('zettel_view', zettel_id=zettel.id))
        except IntegrityError:
            flash("A Zettel with that Title and/or Luhmann ID already exists! Please try again!")
            return redirect(url_for('label_zettel_view'))

    return render_template('views/label_zettel.html', context={'title': 'Label Zettel', 'form': form})


# Route for 'Success' page
@app.route('/success')
def success_view():
    return render_template('views/success.html', context={'title': 'Success'})


# Route for 'Admin' page
@app.route('/admin')
@login_required
def admin_view():
    if current_user.role == RolesEnum.ADMIN.value:
        session = app.Session()
        users = session.query(User).all()
        return render_template('views/admin.html', context={'title':'Admin Area', 'RolesEnum': RolesEnum, 'users':users})
    flash('You are not an admin!')
    return redirect(url_for('index_view'))


@app.route('/bottleneck')
# @cache.cached()  # caches the WHOLE view
def bottleneck_view():
    app.logger.info(f'Time upon request: {dt.datetime.now()}')
    title = cache.get('title')
    if title is None:
        time.sleep(10)
        cache.set('title', 'Bottleneck Area')
    app.logger.info(f'Time upon response: {dt.datetime.now()}')
    return render_template('views/bottleneck.html', context={'title':title})


@app.route('/delete/<int:zettel_id>')
@login_required
def delete_zettel(zettel_id):
    session = app.Session()
    zettel = session.query(Zettel).get(zettel_id)
    session.delete(zettel)
    session.commit()
    flash(f"[{zettel.luhmann_identifier} {zettel.title}] was deleted")
    return redirect(url_for('index_view'))