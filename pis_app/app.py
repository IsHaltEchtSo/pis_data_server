from flask import Flask
from flask_login import LoginManager
from flask_caching import Cache


login_manager = LoginManager()
cache = Cache(config={  'CACHE_TYPE': 'SimpleCache', 
                        'CACHE_DEFAULT_TIMEOUT': 300})


class MyFlask(Flask):
    def get_db_session(self):
        return self._DBSession()


def create_app() -> MyFlask:
    app = MyFlask(__name__, instance_relative_config=True)

    app_initializer = AppInitializer(app=app)
    app_initializer.init_app()

    return app


class AppInitializer:
    def __init__(self, app: Flask) -> None:
        self.flask_app = app


    def init_views(self) -> None:
        """
        Initialize the views using local imports after instantiating an app.
        This is called within the app context to avoid the app context error.
        """
        import pis_app.routes
        import pis_app.auth

        from .auth import auth_bp
        self.flask_app.register_blueprint(auth_bp)

        from .zettelkasten import zk_bp
        self.flask_app.register_blueprint(zk_bp)


    def init_database(self) -> None:
        """
        Initialize the database and locally import the models in app context
        """
        from pis_app.database import Session

        self.flask_app._DBSession = Session


    def init_app_in_ctx(self) -> None:
        """
        Delegate to methods that need the app context to init the app.
        """
        self.init_database()
        self.init_views()


    def configure_app(self) -> None:
        # Load Dev Config if no config object is provided
        try:
            from instance.private_config import DevelopmentConfig
        except ModuleNotFoundError:
            from pis_app.config import DevelopmentConfig
        
        self.flask_app.config.from_object(DevelopmentConfig)


    def init_app(self) -> None:
        """
        Main method that delegates to other methods to fully initialize the app.
        """
        self.configure_app()

        login_manager.init_app(self.flask_app)
        cache.init_app(self.flask_app)

        with self.flask_app.app_context():
            self.init_app_in_ctx()
