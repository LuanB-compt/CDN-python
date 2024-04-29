import flask
import flask_cors
from src.configer.flask import configs
from src.database import MongoDB

def create_app():
    """
    Create the app server with Flask.

    Args:
        test_config (any): Defaults to None.

    Returns:
        flask.Flask
    """
    app = flask.Flask(__name__, instance_relative_config=True)
    
    flask_cors.CORS(app=app)
    app.config.from_object(configs['dev'])
    MongoDB.mongo_client.init_app(app=app)

    with app.app_context():
        return app
