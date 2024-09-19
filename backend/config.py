from os import path, environ

BASEDIR = path.abspath(path.dirname(__file__))

class Config:
    """Base config."""
    DEBUG = False
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASEDIR, 'dev_socialmedia.db')

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    # add postgresql path
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASEDIR, 'todo_data.db') 
