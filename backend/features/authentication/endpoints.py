from ..authentication import authentication_blueprint
from .controller import login, logout



authentication_blueprint.add_url_rule(rule = '/login',
                                      endpoint = 'login',
                                      methods = ['POST', 'GET'],
                                      view_func = login )

authentication_blueprint.add_url_rule(rule = '/logout',
                                      endpoint = 'logout',
                                      methods = ['GET'],
                                      view_func = logout )


