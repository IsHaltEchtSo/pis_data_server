from venv import create
import pytest

from pis_app.app import create_app
from pis_app.models import UpdatedColumn, User, Zettel, ZettelUpdate
from pis_app.config import TestingConfig
from pis_app.database import Base, Session

# --------
# Fixtures
# --------

@pytest.fixture(scope='module')
def user():
    user = User(name='max mustermann')
    return user


@pytest.fixture(scope='module')
def zettel():
    zettel = Zettel(luhmann_identifier='1', title='Zettelkasten', content='')
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
    flask_app = create_app(config_object=TestingConfig)

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
    zettel1 = Zettel(luhmann_identifier='1', title='Zettelkasten')
    zettel2 = Zettel(luhmann_identifier='1a', title='Basic Usage')

    session.add_all([zettel1, zettel2])
    session.commit()

    yield

    # Teardown the Database
    Base.metadata.drop_all()




