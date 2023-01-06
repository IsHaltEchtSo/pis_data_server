from flask import Flask
from flask_login import LoginManager



login_manager = LoginManager()


class MyFlask(Flask):
    DatabaseSession = None


def create_application() -> MyFlask:
    backend_application = MyFlask(__name__, 
                                  instance_relative_config = True, 
                                  template_folder = 'views' )
    BackendInitializer() \
        .start(backend_application)

    return backend_application


class BackendInitializer:
    application: MyFlask = None


    def start(self, input_application: MyFlask) -> None:
        """
        Main method that delegates to other methods to fully initialize the app.
        """
        self.application = input_application

        self._set_application_configuration()
        self._load_external_features()

        with self.application.app_context():
            self._initialize_application_in_context()


    def _set_application_configuration(self) -> None:
        # Load Dev Config if no config object is provided
        try:
            from .instance.private_config import DevelopmentConfig
        except ModuleNotFoundError:
            from .config import DevelopmentConfig
        
        self.application.config.from_object(DevelopmentConfig)


    def _load_external_features(self):
        login_manager.init_app(self.application)


    def _initialize_application_in_context(self) -> None:
        """
        Delegate to methods that need the app context to init the app.
        """
        self._integrate_database()
        self._integrate_features()

        from backend.features.authentication.controller import login

        self.application.add_url_rule(rule = '/',
                                      endpoint = 'authentication_blueprint.login',
                                      methods = ['GET'],
                                      view_func = login )


    def _integrate_database(self) -> None:
        """
        Initialize the database and locally import the models in app context
        """
        from .database import Session

        self.application.DatabaseSession = Session


    def _integrate_features(self) -> None:
        from .features.authentication import authentication_blueprint
        from .features.errorhandling import errorhandling_blueprint
        from .features.index import index_blueprint
        from .features.meditation import meditation_blueprint
        from .features.permissions import permissions_blueprint
        from .features.routine import routine_blueprint
        from .features.task import task_blueprint
        from .features.zettelkasten import zettelkasten_blueprint
        
        self.application.register_blueprint( authentication_blueprint )
        self.application.register_blueprint( errorhandling_blueprint )
        self.application.register_blueprint( index_blueprint )
        self.application.register_blueprint( meditation_blueprint )
        self.application.register_blueprint( permissions_blueprint )
        self.application.register_blueprint( routine_blueprint )
        self.application.register_blueprint( task_blueprint )
        self.application.register_blueprint( zettelkasten_blueprint )

        




    


    


