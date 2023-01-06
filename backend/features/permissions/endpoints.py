from ..permissions import permissions_blueprint

from .controller import main, signup


permissions_blueprint.add_url_rule(rule = '/main',
                                   endpoint = 'main',
                                   view_func = main,
                                   methods = ['GET'] )

permissions_blueprint.add_url_rule(rule = '/signup',
                                   endpoint = 'signup',
                                   view_func = signup,
                                   methods = ['GET', 'POST'] )
