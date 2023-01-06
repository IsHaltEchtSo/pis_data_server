from .models import Meditation

from flask_wtf import FlaskForm
from sqlalchemy.orm import Session



class MeditationFactory():
    """Instantiates Meditation objects using the 'create_meditation' method"""
    def __init__(self, form: FlaskForm, database_session: Session):
        self.form = form
        self.database_session = database_session

    def create_meditation(self) -> Meditation:
        meditation = self._meditation_instantiation()
        return meditation

    def update_meditation(self, meditation: Meditation) -> Meditation:
        self._update_data(meditation)
        return meditation

    def _meditation_instantiation(self) -> Meditation:
        meditation = Meditation(name = self.form.name.data,
                                description = self.form.description.data )
        return meditation

    def _update_data(self, meditation: Meditation) -> None:
        if self.form.name.data:
            meditation.name = self.form.name.data

        if self.form.description.data:
            meditation.description = self.form.description.data


class DatabaseSessionProcessor:
    """Session Processor that helps with updating the Meditation Objects in the Database"""
    def __init__(self, database_session: Session):
        self.database_session = database_session

    def delete_from_database(self, object):
        self.database_session.delete(object)
        self.database_session.commit()

    def add_to_database(self, object):
        self.database_session.add(object)
        self.database_session.commit()