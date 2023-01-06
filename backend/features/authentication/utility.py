from ..permissions.models import User
from backend.application import login_manager

from flask import current_app as app, flash, redirect, url_for



@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged in on every page load"""
    if user_id is not None:
        session = app.DatabaseSession()
        return session.query(User).get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized user to index view"""
    flash('You must be logged in to be able to access this page')
    return redirect(url_for('index_view'))