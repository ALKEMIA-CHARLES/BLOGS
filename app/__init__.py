from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
login_manager = LoginManager()
# security level, monitor the changes in a user's request header and log the user out
login_manager.session_protection = "strong"
# We prefix the login endpoint with the blueprint name because it is located inside a blueprint.
login_manager.login_view = "auth.login"

bootstrap = Bootstrap()


def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)

    # Initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Registering the main app Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Registering auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/authenticate")

    # Setting requests config
    from .requests import configure_request
    configure_request(app)

    return app
