from flask import Blueprint



zettelkasten_blueprint = Blueprint('zettelkasten_blueprint',
                                   __name__,
                                   template_folder='views',
                                   url_prefix='/zettelkasten')

from .endpoints import *