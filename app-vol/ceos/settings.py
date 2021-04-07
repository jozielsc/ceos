# coding: utf-8
import os

class Config(object):
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret-string')
    BCRYPT_LOG_ROUNDS = os.getenv('BCRYPT_LOG_ROUNDS', 6)
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS=os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    HOSTNAME=os.getenv('HOSTNAME', '0.0.0.0')
    PORT=os.getenv('PORT', 5000),
    USE_RELOADER = os.getenv('USE_RELOADER', False)
    USE_DEBUGGER = os.getenv('USE_DEBUGGER', False)
    DB_PASSWD = os.getenv('DB_PASSWD', None)

class DevelopmentConfig(Config):
    FLASK_ENV='development'
    DEBUG = True
    USE_RELOADER = True
    USE_DEBUGGER = True
    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:postgres@127.0.0.1/dev_f'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/prod.db'

class TestingConfig(Config):
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True
    USE_RELOADER = True
    TESTING = True
    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:postgres@127.0.0.1/test_f'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

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
