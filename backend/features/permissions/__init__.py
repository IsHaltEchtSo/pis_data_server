from flask import Blueprint



permissions_blueprint = Blueprint('permissions_blueprint',
                                  __name__,
                                  template_folder = 'views',
                                  url_prefix = '/permissions' )

from .endpoints import *