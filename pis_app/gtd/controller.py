from .models import Task

from flask import (
    current_app as app, 
    render_template,
    Blueprint)



gtd_bp = Blueprint(
            'gtd_bp', 
            __name__,
            template_folder='views',)


@gtd_bp.route('/todoist-clone')
def main():
    session = app.get_db_session()
    daily_tasks = session.query(Task) \
                            # .filter(Task.daily == True) \.all()
    return render_template('gtd/main.html',
                            context={'title':'Todoist Clone',
                                     'daily_tasks': daily_tasks })