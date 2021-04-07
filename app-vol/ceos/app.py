# coding: utf-8
from os import path

from flask import Flask

from ceos.db import db
from ceos.settings import app_config
from ceos.auth.route import auth

def create_app(config_name=None, extra_config=None):

    app = Flask(
        __name__,
        instance_path=path.abspath(path.dirname(__file__)),
        instance_relative_config=True
    )

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('settings.py')

    if extra_config:
        app.config.update(**extra_config)

    db.init_app(app)

    with app.app_context():
        db.session.close()
        # db.drop_all()
        db.create_all()

    app.register_blueprint(auth, url_prefix='/api/auth')

    return app
