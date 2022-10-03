from flask import Flask
from .config import DevelopmentConfig



def create_app():
    app = Flask(__name__, )

    try:
        app.config.from_object(DevelopmentConfig)

        app_initializer = AppInitializer(app=app)
        app_initializer.init_app()

        return app

    except Exception as ex:
        raise ex


class AppInitializer:
    def __init__(self, app: Flask) -> None:
        self.flask_app = app
        self.config = app.config

    def init_views(self) -> None:
        """
        Initialize the views using local imports after instantiating an app.
        This is called within the app context to avoid the app context error.
        """
        import pis_app.routes

    def init_database(self) -> None:
        """
        Initialize the database and locally import the models in app context
        """
        from pis_app.database import Session
        import pis_app.models

        self.flask_app.Session = Session

    def init_app_in_ctx(self) -> None:
        """
        Delegate to methods that need the app context to init the app.
        """
        self.init_database()
        self.init_views()

    def init_app(self) -> None:
        """
        Main method that delegates to other methods to fully initialize the app.
        """
        with self.flask_app.app_context():
            self.init_app_in_ctx()