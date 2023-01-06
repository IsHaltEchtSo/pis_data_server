from flask import Blueprint



task_blueprint = Blueprint('task_blueprint', 
                           __name__,
                           url_prefix = '/task',
                           template_folder = 'views' )

from .endpoints import *