from flask import Flask
from flask_login import LoginManager



login_manager = LoginManager()


class MyFlask(Flask):
    def get_db_session(self):
        return self._DBSession()


def create_app() -> MyFlask:
    app = MyFlask(  __name__, 
                    instance_relative_config=True, 
                    template_folder='templates')

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
        from .main_feature import main_blueprint
        self.flask_app.register_blueprint(main_blueprint)

        from .auth_feature import auth_blueprint
        self.flask_app.register_blueprint(auth_blueprint)

        from .zettelkasten_feature import zettelkasten_blueprint
        self.flask_app.register_blueprint(zettelkasten_blueprint)

        from .admin_feature import admin_blueprint
        self.flask_app.register_blueprint(admin_blueprint)

        from .tasks_feature import tasks_blueprint
        self.flask_app.register_blueprint(tasks_blueprint)

        from .routine_feature import routine_blueprint
        self.flask_app.register_blueprint(routine_blueprint)


    def init_database(self) -> None:
        """
        Initialize the database and locally import the models in app context
        """
        from .database import Session

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
            from .instance.private_config import DevelopmentConfig
        except ModuleNotFoundError:
            from .config import DevelopmentConfig
        
        self.flask_app.config.from_object(DevelopmentConfig)


    def init_app(self) -> None:
        """
        Main method that delegates to other methods to fully initialize the app.
        """
        self.configure_app()

        login_manager.init_app(self.flask_app)

        with self.flask_app.app_context():
            self.init_app_in_ctx()
