"""
See 'rsc/Redirect_Backbone.png' for a diagram of the resource hierarchy.
"""
from flask import render_template, current_app as app


# Route for 'Home' page
@app.route('/')
@app.route('/index')
def index_view():
    return render_template('views/index.html')


# Route for 'Login' page
@app.route('/login')
def login_view():
    return render_template('views/login.html')


# Route for 'History' page
@app.route('/history')
def history_view():
    return render_template('views/history.html')


# Route for 'Manual' page
@app.route('/manual')
def manual_view():
    return render_template('views/manual.html')


# Route for 'Zettel Search' page
@app.route('/zettel_search')
def zettel_search_view():
    return render_template('views/zettel_search.html')


# Route for 'Zettel Search Results' page
@app.route('/zettel_search_results')
def zettel_search_results_view():
    return render_template('views/zettel_search_results.html')


# Route for 'Zettel' page
@app.route('/zettel')
def zettel_view():
    return render_template('views/zettel.html')


# Route for 'Zettel Edit' page
@app.route('/zettel_edit')
def zettel_edit_view():
    return render_template('views/zettel_edit.html')


# Route for 'Checklist' page
@app.route('/checklist')
def checklist_view():
    return render_template('views/checklist.html')


# Route for 'Digitalize Zettel' page
@app.route('/digitalize_zettel')
def digitalize_zettel_view():
    return render_template('views/digitalize_zettel.html')


# Route for 'Label Zettel' page
@app.route('/label_zettel')
def label_zettel_view():
    return render_template('views/label_zettel.html')


# Route for 'Success' page
@app.route('/success')
def success_view():
    return render_template('views/success.html')