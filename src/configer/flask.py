import os
basedir = os.path.abspath(path="./")


class Config:
    """
    Parent configuration, which is commom in others configurations.
    """
    SQLALCHEMY_ECHO = True


class DevConfig(Config):
    """
    Development configurations.

    Args:
        Config (class): inheritance received.
    """
    FLASK_ENV = "development"
    FLASK_DEBUG = True
    TESTING = True
    MONGO_URI = "mongodb://127.0.0.1:27017/CDN_dev"


class ProdConfig(Config):
    """
    Production configurations.

    Args:
        Config (class): inheritance received.
    """
    FLASK_ENV = "production"
    FLASK_DEBUG = False
    TESTING = False
    MONGO_URI = "mongodb://127.0.0.1:27017/CDN"


configs = {"dev": DevConfig, "prod": ProdConfig}