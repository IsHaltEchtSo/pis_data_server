from backend.meditation_feature import meditation_blueprint
from .controller import main, create, view, edit, delete



meditation_blueprint.add_url_rule(rule = '/main',
                                  methods = ['GET'],
                                  endpoint = 'main',
                                  view_func = main )


meditation_blueprint.add_url_rule(rule = '/create',
                                  methods = ['POST', 'GET'],
                                  endpoint = 'create',
                                  view_func = create )


meditation_blueprint.add_url_rule(rule = '/view/<meditation_id>',
                                  methods = ['GET'],
                                  endpoint = 'view',
                                  view_func = view ) 


meditation_blueprint.add_url_rule(rule = '/edit/<meditation_id>',
                                  methods = ['POST', 'GET'],
                                  endpoint = 'edit',
                                  view_func = edit )


meditation_blueprint.add_url_rule(rule = '/delete/<meditation_id>',
                                  methods = ['POST', 'GET'],
                                  endpoint = 'delete',
                                  view_func = delete )


