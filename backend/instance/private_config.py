"""
Holds the Config classes, which are used to store the configurations of the app.
"""
from logging.config import dictConfig as loggerConfig


class Config:
    TESTING = False
    SECRET_KEY = """some2345very2 -345e24key34008saΩ45e24key4key45e24keyω∑45e24keyθfe23405q234e4key23ω∑θfe2
    4008saΩω∑8uω∑θfe2-324key-982ω∑θfe24r9908saΩω∑90sdf*)HJ_*h@@‹›€‹€
    """

class ProductionConfig(Config):
    DATABASE_URI = 'postgresql+psycopg2://deniz@localhost:5454/zettelkasten'

class DevelopmentConfig(Config):
    DATABASE_URI = 'postgresql+psycopg2://deniz@localhost:5454/zettelkasten'

class TestingConfig(Config):
    DATABASE_URI = 'postgresql+psycopg2://deniz@localhost:5454/test_db'
    TESTING = True

# loggerConfig(
#     {
#         "version": 1,
#         "formatters": {
#             "default": {
#                 "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
#                 "datefmt": "%d.%m.%Y %H:%M:%S %Z",
#             },
#             "short": {
#                 "format": "%(levelname)s in %(module)s: %(message)s"
#             }
#         },
#         "handlers": {
#             "console": {
#                 "class": "logging.StreamHandler",
#                 "stream": "ext://sys.stdout",
#                 "formatter": "short",
#             },
#             "file": {
#                 "class": "logging.FileHandler",
#                 "filename": "instance/logger.log",
#                 "formatter": "default",
#             },
#         },
#         "root": {"level": "ERROR", "handlers": ["console", "file"]},
#     }
# )
