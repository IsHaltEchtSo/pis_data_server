from flask import render_template



def page_not_found(error):
    return render_template('errorhandling/404.jinja2', 
                           data = {'error': error } )