from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired



class MeditationForm(FlaskForm):
    name        = StringField(label = 'Meditation',
                              validators = [ DataRequired()])

    description = TextAreaField(label = 'Description',
                                validators = [ DataRequired()])

    submit      = SubmitField(label = 'Submit')