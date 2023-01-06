from flask import Blueprint



errorhandling_blueprint = Blueprint('errorhandling_blueprint',
                                    __name__,
                                    template_folder = 'views',
                                    url_prefix = '/error')

from .endpoints import *