from .models import Task

from flask import current_app as application, render_template, url_for


def main():
    daily_tasks = application.DatabaseSession().query(Task) \
                                               .all()
    return render_template('task/main.jinja2',
                            data = {'feature_title': 'Task',
                                    'feature_url': url_for('test_blueprint.main'), 
                                    'daily_tasks': daily_tasks } )