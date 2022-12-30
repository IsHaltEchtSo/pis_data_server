from backend.meditation_feature import meditation_blueprint
from .controller import main, meditation_create



meditation_blueprint.add_url_rule(rule = '/main',
                                  methods = ['GET'],
                                  endpoint = 'main',
                                  view_func = main )


meditation_blueprint.add_url_rule(rule = '/create',
                                  methods = ['POST', 'GET'],
                                  endpoint = 'create',
                                  view_func = meditation_create )



