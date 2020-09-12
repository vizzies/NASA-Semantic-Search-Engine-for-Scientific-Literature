from os import environ


class Config(object):
    """Base config."""
    STATIC_FOLDER = "static"
    TESTING = False
    SQLALCHEMY_ECHO = False
    CELERY_BROKER_URL = environ.get("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = environ.get("CELERY_RESULT_BACKEND_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GITHUB_TOKEN = environ.get("GITHUB_TOKEN")
    GITHUB_BASE_URL = "https://api.github.com/graphql"
    GOV_ORGS_FP = ("https://raw.githubusercontent.com"
                   "/github/government.github.com"
                   "/gh-pages/_data/governments.yml")

class ProdConfig(Config):
    """Production config"""
    FLASK_ENV = "production"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = environ.get("PROD_DATABASE_URI")


class DevConfig(Config):
    """Development config"""
    FLASK_ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get("DEV_DATABASE_URI")


class TestConfig(DevConfig):
    """Testing config"""
    SQLALCHEMY_DATABASE_URI = environ.get("TEST_DATABASE_URI")
    TESTING = True
