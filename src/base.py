import flask
from src.configer.flask import configs

def create_app():
    """
    Create the app server with Flask.

    Args:
        test_config (any): Defaults to None.

    Returns:
        flask.Flask
    """
    app = flask.Flask(__name__, instance_relative_config=True)
    app.config.from_object(configs['dev'])

    with app.app_context():
        return app