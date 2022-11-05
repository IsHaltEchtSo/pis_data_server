"""
See 'rsc/Redirect_Backbone.png' for a diagram of the resource hierarchy.
"""
#TODO: CUD operations make a new Zettel Update
from flask import render_template, current_app as app, redirect, flash, url_for
from flask_login import login_required, current_user
from .models import RolesEnum, User
from .app import cache
import time


# Route for 'Home' page
@app.route('/')
@app.route('/index')
def index_view():
    return render_template('views/index.html', context={'title': 'Index', 'RolesEnum': RolesEnum})


# Route for 'History' page
@app.route('/history')
@login_required
def history_view():
    return render_template('views/history.html', context={'title': 'History'})


# Route for 'Manual' page
@app.route('/manual')
def manual_view():
    return render_template('views/manual.html', context={'title': 'Manual'})


# Route for 'Zettel Search' page
@app.route('/zettel_search')
def zettel_search_view():
    return render_template('views/zettel_search.html', context={'title': 'Zettel Search'})


# Route for 'Zettel' page
@app.route('/zettel')
def zettel_view():
    return render_template('views/zettel.html', context={'title': 'Zettel'})


# Route for 'Zettel Edit' page
@app.route('/zettel_edit')
def zettel_edit_view():
    return render_template('views/zettel_edit.html', context={'title': 'Zettel Edit'})


# Route for 'Checklist' page
@app.route('/checklist')
def checklist_view():
    return render_template('views/checklist.html', context={'title': 'Checklist'})


# Route for 'Digitalize Zettel' page
@app.route('/digitalize_zettel')
def digitalize_zettel_view():
    return render_template('views/digitalize_zettel.html', context={'title': 'Digitalize Zettel'})


# Route for 'Label Zettel' page
@app.route('/label_zettel')
def label_zettel_view():
    return render_template('views/label_zettel.html', context={'title': 'Label Zettel'})


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
@cache.cached()
def bottleneck_view():
    time.sleep(10)
    return render_template('views/bottleneck.html', context={'title':'Bottleneck Area'})