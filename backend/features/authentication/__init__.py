from flask import Blueprint



authentication_blueprint = Blueprint('authentication_blueprint',
                                     __name__,
                                     template_folder='views',
                                     url_prefix='/authentication')


from .endpoints import *