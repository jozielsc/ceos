# coding: utf-8
from os import path

from flask import Flask
# from flask_restx import Api
#
from werkzeug.middleware.proxy_fix import ProxyFix

from ceos.settings import app_config
# from ceos.db import db, ma
# from ceos.pseudocrawler.route import app as crawler

from ceos.resttest.namespace import blueprint as api
from ceos.lysis.namespace import blueprint as lysis

def create_app(config_name=None, extra_config=None):

    app = Flask(
        __name__,
        instance_path=path.abspath(path.dirname(__file__)),
        instance_relative_config=True
    )

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('settings.py')

    if extra_config:
        app.config.update(**extra_config)



    # db.init_app(app)
    # ma.init_app(app)
    #
    # app.register_blueprint(crawler, url_prefix='/crawler')

    app.register_blueprint(api, url_prefix='/api/v1')
    app.register_blueprint(lysis, url_prefix='/api/v2')

    return app
