"""
Holds the standard config classes, which are used to store the configurations of the app.
Please override them in a 'local_config.py' file.
"""
from logging.config import dictConfig as loggerConfig

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

loggerConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                "datefmt": "%d.%m.%Y %H:%M:%S %Z",
            },
            "short": {
                "format": "%(levelname)s in %(module)s: %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "short",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": "instance/logger.log",
                "formatter": "default",
            },
        },
        "root": {"level": "INFO", "handlers": ["console", "file"]},
    }
)
