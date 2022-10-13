"""
Holds the standard config classes, which are used to store the configurations of the app.
Please override them in a 'local_config.py' file.
"""

class Config:
    TESTING = False
    SECRET_KEY = """please change me"""

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DATABASE_URI = 'postgresql+psycopg2://deniz@localhost:5454/zettelkasten'

class TestingConfig(Config):
    DATABASE_URI = 'postgresql+psycopg2://deniz@localhost:5454/test_db'
    TESTING = True