from ..task import task_blueprint
from .controller import main



task_blueprint.add_url_rule(rule = 'main',
                            endpoint = '/main',
                            methods = ['GET'],
                            view_func = main )