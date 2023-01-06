from flask import Blueprint



meditation_blueprint = Blueprint('meditation_blueprint',
                                 __name__,
                                 template_folder='views',
                                 url_prefix='/meditation')

from .endpoints import *
