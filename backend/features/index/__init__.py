from flask import Blueprint


index_blueprint = Blueprint('index_blueprint',
                            __name__,
                            template_folder='views',
                            url_prefix='/')


from .endpoints import *