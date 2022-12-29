from .models import Task

from flask import (
    current_app as app, 
    render_template,
    Blueprint)



tasks_blueprint = Blueprint('tasks_blueprint', 
                            __name__,
                            template_folder='views',)


@tasks_blueprint.route('/todoist-clone')
def main():
    session = app.get_db_session()
    daily_tasks = session.query(Task) \
                            # .filter(Task.daily == True) \.all()
    return render_template('tasks/main.jinja2',
                            data={'title':'Todoist Clone',
                                  'daily_tasks': daily_tasks })