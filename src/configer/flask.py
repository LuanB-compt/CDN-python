import os
basedir = os.path.abspath(path="./")


class Config:
    """
    Parent configuration, which is commom in others configurations.
    """
    SQLALCHEMY_ECHO = True
    UPLOAD_FOLDER = "uploads"


class DevConfig(Config):
    """
    Development configurations.

    Args:
        Config (class): inheritance received.
    """
    FLASK_ENV = "development"
    FLASK_DEBUG = True
    TESTING = True


class ProdConfig(Config):
    """
    Production configurations.

    Args:
        Config (class): inheritance received.
    """
    FLASK_ENV = "production"
    FLASK_DEBUG = False
    TESTING = False


configs = {"dev": DevConfig, "prod": ProdConfig}