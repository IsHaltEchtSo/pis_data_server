from backend.constants import RolesEnum

from flask import render_template



def main():
    return render_template('index/main.jinja2', 
                            data = {'title': 'Index', 
                                    'RolesEnum': RolesEnum } )