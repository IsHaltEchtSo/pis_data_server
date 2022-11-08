from flask import current_app as app, render_template


@app.errorhandler(404)
def not_found(e):
    return render_template('views/404.html', context={'e':e})