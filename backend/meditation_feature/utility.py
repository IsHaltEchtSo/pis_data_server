from .models import Meditation

from flask_wtf import FlaskForm
from sqlalchemy.orm import Session



class MeditationFactory():
    """Instantiates Meditation objects using the 'create_meditation' method"""
    def __init__(self, form: FlaskForm, db_session: Session):
        self.form = form
        self.db_session = db_session

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


class DBSessionProcessor:
    """Session Processor that helps with updating the Meditation Objects in the Database"""
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def delete_from_db(self, object):
        self.db_session.delete(object)
        self.db_session.commit()

    def add_to_db(self, object):
        self.db_session.add(object)
        self.db_session.commit()