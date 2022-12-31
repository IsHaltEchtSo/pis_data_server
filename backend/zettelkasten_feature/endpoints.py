from backend.zettelkasten_feature import zettelkasten_blueprint
from backend.zettelkasten_feature.controller import main, create, search, view, edit, delete



zettelkasten_blueprint.add_url_rule(rule = '/main',
                                    methods = ['GET'],
                                    endpoint = 'main',
                                    view_func = main )


zettelkasten_blueprint.add_url_rule(rule = '/create',
                                    methods = ['POST', 'GET'],
                                    endpoint = 'create',
                                    view_func = create )


zettelkasten_blueprint.add_url_rule(rule = '/view/<luhmann_id>',
                                    methods = ['GET'],
                                    endpoint = 'view',
                                    view_func = view ) 


zettelkasten_blueprint.add_url_rule(rule = '/edit/<luhmann_id>',
                                    methods = ['POST', 'GET'],
                                    endpoint = 'edit',
                                    view_func = edit )


zettelkasten_blueprint.add_url_rule(rule = '/delete/<luhmann_id>',
                                    methods = ['POST', 'GET'],
                                    endpoint = 'delete',
                                    view_func = delete )

zettelkasten_blueprint.add_url_rule(rule = '/search',
                                    methods = ['POST', 'GET'],
                                    endpoint = 'search',
                                    view_func = search )


