"""Form for Zettel-related stuff."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired



class ZettelSearchForm(FlaskForm):
    """ZettelSearch Form"""
    luhmann_id  = StringField(
                    label='Luhmann ID',)

    title       = StringField(
                    label='Title')

    submit      = SubmitField(
                    label='Search')


class ZettelEditForm(FlaskForm):
    """Form to edit Zettel"""
    luhmann_id  = StringField(
                    label='Luhmann ID')

    title       = StringField(
                    label='Title')

    content     = TextAreaField(
                    label='Content')

    links       = StringField(
                    label="Links")

    backlinks   = StringField(
                    label="Backlinks")

    submit      = SubmitField(
                    label='Save')


class DigitaliseZettelForm(FlaskForm):
    """Form to capture data for new Zettels"""
    luhmann_id  = StringField(
                    label='Luhmann ID',
                    validators=[
                        DataRequired()])

    title       = StringField(
                    label='Title',
                    validators=[
                        DataRequired()])

    content     = TextAreaField(
                    label='Content')

    links       = StringField(
                    label='Links')

    backlinks   = StringField(
                    label='Backlinks')
                    
    submit      = SubmitField(
                    label='Save')

