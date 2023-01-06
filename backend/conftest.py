from .application import create_application
from .config import TestingConfig
from .database import Base, Session
from .features.zettelkasten.models import UpdatedColumn, User, Zettel, ZettelUpdate

import pytest



@pytest.fixture(scope='module')
def user():
    user = User(name='max mustermann')
    return user


@pytest.fixture(scope='module')
def zettel():
    zettel = Zettel(luhmann_id='1', title='Zettelkasten', content='')
    return zettel


@pytest.fixture(scope='module')
def updated_column():
    new_updated_column = UpdatedColumn(column_name='title', old_column_value='Zettelkasten', new_column_value='The Zettelkasten')
    return new_updated_column


@pytest.fixture(scope='module')
def zettel_update(zettel, updated_column):
    new_zettel_update = ZettelUpdate(zettel=zettel, updated_columns=[updated_column])
    return new_zettel_update


@pytest.fixture(scope='module')
def test_client():
    # Create a Flask App configured for testing
    flask_app = create_application(config_object = TestingConfig)

    # Create a Test Client using the Flask Application
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


@pytest.fixture(scope='module')
def session(test_client):
    """A session fixture used to interact with the database"""
    session = Session()
    yield session

    session.close()


@pytest.fixture(scope='module')
def init_database(test_client, session):
    # Setup Database Tables
    Base.metadata.create_all()

    # Populate the DB
    zettel1 = Zettel(luhmann_id='1', title='Zettelkasten')
    zettel2 = Zettel(luhmann_id='1a', title='Basic Usage')

    session.add_all([zettel1, zettel2])
    session.commit()

    yield

    # Teardown the Database
    Base.metadata.drop_all()




