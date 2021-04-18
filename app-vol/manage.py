# coding: utf-8

import os
import unittest
import redis

from flask.cli import FlaskGroup
from ceos.app import create_app as ceos
from ceos.db import db

def create_app(script_info=None):
    config_name=os.environ.get("FLASK_ENV", default="production")
    app = ceos(config_name=config_name)
    cache = redis.Redis(host='redis', port=6379)

    @app.shell_context_processor
    def shell_context():
        return {
            'app': app,
            'redis': cache
        }

    return app

cli = FlaskGroup(create_app=create_app)

@cli.command('test')
def test():
    """Run all scripts in dir tests/test*.py """
    tests = unittest.TestLoader().discover('./tests', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@cli.command("create_db")
def recreate_db():
    """Create all db"""
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()
