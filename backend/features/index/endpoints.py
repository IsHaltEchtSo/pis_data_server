from ..index import index_blueprint
from .controller import main



index_blueprint.add_url_rule(rule = '/index/main',
                             endpoint = 'main',
                             methods = ['GET'],
                             view_func = main)