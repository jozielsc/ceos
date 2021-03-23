# coding: utf-8
from os import path

from flask_api import FlaskAPI

from .settings import app_config
# from .bucketlist.route import bucket
# from .auth.route import auth
from .relationship.route import blueprint as relationship
from .db import db

def create_app(config_name=None, extra_config=None):

    app = FlaskAPI(
        "ceos",
        instance_path=path.abspath(path.dirname(__file__)),
        instance_relative_config=True
    )

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('settings.py')

    if extra_config:
        app.config.update(**extra_config)

    db.init_app(app)

    # app.register_blueprint(bucket, url_prefix='/api/v1/bucketlists')
    # app.register_blueprint(auth, url_prefix='/api/v1/auth')
    app.register_blueprint(relationship, url_prefix='/api/v1/relationship')

    return app
