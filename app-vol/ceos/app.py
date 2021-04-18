# coding: utf-8
from os import path

from flask import Flask

from ceos.db import db, ma
from ceos.settings import app_config
from ceos.pseudocrawler.route import app as crawler

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
    ma.init_app(app)

    app.register_blueprint(crawler, url_prefix='/crawler')

    return app
