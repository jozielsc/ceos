# coding: utf-8

import os
import unittest
from flask.cli import FlaskGroup
from ceos.app import create_app as ceos

def create_app(script_info=None):

    app = ceos(config_name="testing")

    @app.shell_context_processor
    def shell_context():
        return {'app': app}

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


@cli.command('migrate')
def migrate():
    """Run migrate"""
    pass


if __name__ == '__main__':
    cli()
