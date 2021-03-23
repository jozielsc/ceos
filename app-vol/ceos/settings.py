# coding: utf-8
import os

class Config(object):
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.getenv('SECRET_KEY')
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS=os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    HOSTNAME=os.getenv('HOSTNAME', '0.0.0.0')
    PORT=os.getenv('PORT', 5000),
    USE_RELOADER = os.getenv('USE_RELOADER', False)
    USE_DEBUGGER = os.getenv('USE_DEBUGGER', False)

class DevelopmentConfig(Config):
    FLASK_ENV='development'
    DEBUG = True
    USE_RELOADER = True
    USE_DEBUGGER = True
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:postgres@192.168.1.121/labld'

class TestingConfig(Config):
    DEBUG = True
    USE_RELOADER = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:123@db/test'

class StagingConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    FLASK_ENV='production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
