from flask_wtf import FlaskForm
from wtforms import StringField, TimeField, SubmitField
from wtforms.validators import DataRequired



class RoutineForm(FlaskForm):
    name        = StringField( label = 'Routine',
                               validators = [ DataRequired()])

    starttime   = TimeField( label = 'Starting Time',
                             validators = [ DataRequired()])

    submit      = SubmitField( label = 'Submit')