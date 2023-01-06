from ..errorhandling import errorhandling_blueprint

from .controller import page_not_found



errorhandling_blueprint.register_error_handler(code_or_exception = 404,
                                               f = page_not_found )



